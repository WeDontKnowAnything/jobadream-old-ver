import pandas as pd
import time

import kis_auth as ka
import kis_domstk as kb

# 토큰 발급
ka.auth()

def load_stock_data(file_path: str, sheet_name: str, market: str) -> pd.DataFrame:
    """
    엑셀 파일에서 단축코드, 종목명, 증권그룹구분코드를 불러오고, ST 그룹코드만 필터링합니다.
    
    Args:
        file_path (str): 엑셀 파일 경로
        sheet_name (str): 시트 이름
        market (str): 시장 이름 (KOSPI, KOSDAQ, KONEX)
        
    Returns:
        pd.DataFrame: 필터링된 데이터프레임
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    if market == "KOSPI":
        df = df.rename(columns={"단축코드": "item_code", "한글명": "stock_name", "그룹코드": "group_code"})
    elif market == "KOSDAQ":
        df = df.rename(columns={"단축코드": "item_code", "한글종목명": "stock_name", "증권그룹구분코드": "group_code"})
    elif market == "KONEX":
        df = df.rename(columns={"단축코드": "item_code", "종목명": "stock_name", "증권그룹구분코드": "group_code"})
    
    # ST 그룹코드만 필터링
    df = df[df["group_code"] == "ST"]
    
    return df[["item_code", "stock_name", "group_code"]]

def get_valid_monthly_data(item_code: str, start_date: str) -> pd.DataFrame:
    """
    주어진 종목에 대해 유효한 월별 데이터를 추출합니다.
    
    Args:
        item_code (str): 종목 코드
        start_date (str): 데이터 수집 시작 날짜 (예: '20200101')
        
    Returns:
        pd.DataFrame: 수집된 월별 데이터
    """
    while True:
        # 해당 월의 데이터를 가져옴
        partial_data = kb.get_inquire_daily_itemchartprice(
            itm_no=item_code,
            inqr_strt_dt=start_date,
            period_code="M",
            output_dv="2",
        )
        
        # 유효한 데이터가 있으면 반환
        if not partial_data.empty:
            print(f"{item_code}에 대한 {start_date[:6]} 부터의 데이터 수집 완료")
            return partial_data
        
        # 데이터가 유효하지 않으면 다음 달로 이동
        next_date = pd.to_datetime(start_date, format='%Y%m%d') + pd.DateOffset(months=1)
        start_date = next_date.strftime('%Y%m%d')
        
        # 현재 시점을 넘으면 루프 종료
        if next_date > pd.to_datetime("today"):
            print(f"{item_code}에 대한 유효한 데이터가 없습니다.")
            return pd.DataFrame()

def save_market_data(file_paths: dict, start_date: str, output_filename: str):
    """
    각 시장에서 데이터를 수집하고 CSV 파일로 저장하는 함수.
    
    Args:
        file_paths (dict): 각 시장의 엑셀 파일 경로와 시트 이름을 담은 딕셔너리
        start_date (str): 데이터 수집 시작 날짜 (예: '20200101')
        output_filename (str): 결과를 저장할 CSV 파일 이름
    """
    all_data = pd.DataFrame()

    for market, path_info in file_paths.items():
        print(f"{market} 데이터 수집을 시작합니다.")
        df = load_stock_data(path_info["file_path"], path_info["sheet_name"], market)
        
        for _, row in df.iterrows():
            item_code = row['item_code']
            stock_name = row['stock_name']

            # 유효한 월 데이터를 가져옴
            monthly_data = get_valid_monthly_data(item_code, start_date)
            
            if not monthly_data.empty:
                monthly_data["stock_name"] = stock_name
                monthly_data["item_code"] = item_code
                all_data = pd.concat([all_data, monthly_data], ignore_index=True)
        
        print(f"{market} 데이터 수집 완료.")

    # 모든 데이터를 CSV 파일로 저장
    if not all_data.empty:
        all_data.to_csv(output_filename, index=False)
        print(f"{output_filename} 파일에 저장 완료")
    else:
        print("수집된 데이터가 없어 파일 저장을 건너뜁니다.")

if __name__ == "__main__":
    start_date = "20200101"

    file_paths = {
        "KOSPI": {"file_path": "test/kospi_code.xlsx", "sheet_name": "Sheet1"},
        "KOSDAQ": {"file_path": "test/kosdaq_code.xlsx", "sheet_name": "Sheet1"},
        "KONEX": {"file_path": "test/konex_code.xlsx", "sheet_name": "Sheet1"},
    }

    save_market_data(file_paths, start_date, "stocks_data_markets.csv")