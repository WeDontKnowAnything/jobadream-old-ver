import pandas as pd
import time
import requests
import json
from datetime import datetime, timedelta
from pandas import DataFrame
import kis_auth as kis

# 토큰 발급
kis.auth()


def load_stock_data(file_path: str, sheet_name: str, market: str) -> pd.DataFrame:
    """
    엑셀 파일에서 단축코드, 종목명, 증권그룹구분코드를 불러오고, ST 그룹코드만 필터링합니다.

    Args:
        file_path (str): 엑셀 파일 경로.
        sheet_name (str): 시트 이름.
        market (str): 시장 이름 (KOSPI, KOSDAQ, KONEX).

    Returns:
        pd.DataFrame: 필터링된 데이터프레임.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    if market == "KOSPI":
        df = df.rename(
            columns={
                "단축코드": "item_code",
                "한글명": "stock_name",
                "그룹코드": "group_code",
            }
        )
    elif market == "KOSDAQ":
        df = df.rename(
            columns={
                "단축코드": "item_code",
                "한글종목명": "stock_name",
                "증권그룹구분코드": "group_code",
            }
        )
    elif market == "KONEX":
        df = df.rename(
            columns={
                "단축코드": "item_code",
                "종목명": "stock_name",
                "증권그룹구분코드": "group_code",
            }
        )

    df = df[df["group_code"] == "ST"]
    df["item_code"] = df["item_code"].apply(lambda x: f"{int(x):06d}")

    return df[["item_code", "stock_name", "group_code"]]


def inquire_daily_itemchart_price(
    output_division: str = "1",
    division_code: str = "J",
    item_code: str = "",
    inquiry_start_date: str = None,
    inquiry_end_date: str = None,
    period_code: str = "D",
    adjusted_price: str = "1",
    transaction_cont: str = "",
    fk100: str = "",
    nk100: str = "",
) -> pd.DataFrame:
    """
    국내 주식 기간별 시세 데이터를 가져오는 함수.

    Args:
        output_division (str): 출력 구분 코드.
        division_code (str): 시장 분류 코드.
        item_code (str): 종목 코드.
        inquiry_start_date (str): 조회 시작일자.
        inquiry_end_date (str): 조회 종료일자.
        period_code (str): 기간 분류 코드 (D:일봉, W:주봉, M:월봉, Y:년봉).
        adjusted_price (str): 수정주가 옵션 (0:수정주가, 1:원주가).
        transaction_cont (str): 거래내역.
        fk100 (str): 기타 파라미터.
        nk100 (str): 기타 파라미터.

    Returns:
        pd.DataFrame: 수집된 데이터프레임.
    """
    url = "/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice"
    transaction_id = "FHKST03010100"

    if inquiry_start_date is None:
        inquiry_start_date = (datetime.now() - timedelta(days=100)).strftime("%Y%m%d")
    if inquiry_end_date is None:
        inquiry_end_date = datetime.today().strftime("%Y%m%d")

    params = {
        "FID_COND_MRKT_DIV_CODE": division_code,
        "FID_INPUT_ISCD": item_code,
        "FID_INPUT_DATE_1": inquiry_start_date,
        "FID_INPUT_DATE_2": inquiry_end_date,
        "FID_PERIOD_DIV_CODE": period_code,
        "FID_ORG_ADJ_PRC": adjusted_price,
    }
    response = kis._url_fetch(url, transaction_id, transaction_cont, params)

    if output_division == "1":
        return pd.DataFrame(response.getBody().output1, index=[0])
    else:
        return pd.DataFrame(response.getBody().output2)


def get_valid_monthly_data(item_code: str, start_date: str) -> pd.DataFrame:
    """
    주어진 종목에 대해 유효한 월별 데이터를 추출합니다.

    Args:
        item_code (str): 종목 코드.
        start_date (str): 데이터 수집 시작 날짜 (예: '20200101').

    Returns:
        pd.DataFrame: 수집된 월별 데이터.
    """
    while True:
        partial_data = inquire_daily_itemchart_price(
            itm_no=item_code,
            inqr_strt_dt=start_date,
            period_code="M",
            output_dv="2",
        )

        if not partial_data.empty:
            print(f"{item_code}에 대한 {start_date[:6]} 부터의 데이터 수집 완료")
            return partial_data

        next_date = pd.to_datetime(start_date, format="%Y%m%d") + pd.DateOffset(
            months=1
        )
        start_date = next_date.strftime("%Y%m%d")

        if next_date > pd.to_datetime("today"):
            print(f"{item_code}에 대한 유효한 데이터가 없습니다.")
            return pd.DataFrame()


def save_market_data(file_paths: dict, start_date: str, output_filename: str) -> None:
    """
    각 시장에서 데이터를 수집하고 CSV 파일로 저장하는 함수.

    Args:
        file_paths (dict): 각 시장의 엑셀 파일 경로와 시트 이름을 담은 딕셔너리.
        start_date (str): 데이터 수집 시작 날짜 (예: '20200101').
        output_filename (str): 결과를 저장할 CSV 파일 이름.
    """
    all_data = pd.DataFrame()

    for market, path_info in file_paths.items():
        print(f"{market} 데이터 수집을 시작합니다.")
        df = load_stock_data(path_info["file_path"], path_info["sheet_name"], market)

        for _, row in df.iterrows():
            item_code = row["item_code"]
            stock_name = row["stock_name"]

            monthly_data = get_valid_monthly_data(item_code, start_date)

            if not monthly_data.empty:
                monthly_data["stock_name"] = stock_name
                monthly_data["item_code"] = item_code
                all_data = pd.concat([all_data, monthly_data], ignore_index=True)

        print(f"{market} 데이터 수집 완료.")

    if not all_data.empty:
        all_data.to_csv(output_filename, index=False)
        print(f"{output_filename} 파일에 저장 완료")
    else:
        print("수집된 데이터가 없어 파일 저장을 건너뜁니다.")


def main() -> None:
    start_date = "20200101"

    file_paths = {
        "KOSPI": {"file_path": "test/kospi_code.xlsx", "sheet_name": "Sheet1"},
        "KOSDAQ": {"file_path": "test/kosdaq_code.xlsx", "sheet_name": "Sheet1"},
        "KONEX": {"file_path": "test/konex_code.xlsx", "sheet_name": "Sheet1"},
    }

    save_market_data(file_paths, start_date, "stocks_data_markets.csv")


if __name__ == "__main__":
    main()
