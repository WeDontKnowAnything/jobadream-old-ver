import dart_fss
import pandas as pd
from env import settings


def set_api_key():
    api_key = settings.DART_API_KEY
    dart_fss.set_api_key(api_key=api_key)


# corp = 회사
# listed = 상장
# delisted = 비상장
def get_corps_df() -> pd.DataFrame:
    all_corps = dart_fss.api.filings.get_corp_code()
    all_corps_df = pd.DataFrame(all_corps)
    corps_df = all_corps_df[all_corps_df["stock_code"].notnull()].reset_index(drop=True)
    return corps_df


def get_report(corp_df, corp_name, bsns_year, report_code, fs_div):
    # (1) corp_code : 기업코드
    corp_code = corp_df[corp_df["corp_name"] == corp_name].iloc[
        0, 0
    ]  # corp_df에서 corp_name에 해당하는 corp_code를 찾아 corp_code에 저장

    report_names_list = {
        "11013": "1분기",
        "11012": "반기",
        "11014": "3분기",
        "11011": "사업",
    }  # (3) 1분기보고서 : 11013 반기보고서 : 11012 3분기보고서 : 11014 사업보고서 : 11011
    fs_div = ["CFS", "OFS"]  # (4) CFS : 연결재무제표 OFS : 재무제표
    report_name = report_names_list.get(report_code)

    # 만약 연결제무제표가 없다면 재무제표로 다시 시도
    try:
        data = dart_fss.api.finance.fnltt_singl_acnt_all(
            corp_code, bsns_year, report_code, fs_div, api_key=None
        )["list"]
    except:
        # 해당 사업연도, 분기에 해당하는 재무제표가 없다면 다음 사업연도, 분기로 넘어간다.
        print(f"{corp_name}사의 {bsns_year}년 {report_name} 재무제표가 없습니다.")
        pass
    else:
        financial_report = pd.DataFrame(data)
        financial_report.to_csv(
            f"test_data/{corp_name} {bsns_year}년 {report_name} 재무보고서.csv",
            index=True,
        )


# 상폐 기업 제거 함수
def remove_delisted_corps(corp_df) -> pd.DataFrame:
    # CSV 파일 읽기
    CSV2COMPARE_PATH = "test_data/상장법인목록_2024_08_09.csv"
    compare_df = pd.read_csv(CSV2COMPARE_PATH)

    # 데이터 타입 변환
    corp_df["stock_code"] = corp_df["stock_code"].astype(int)
    compare_df["종목코드"] = compare_df["종목코드"].astype(int)

    # 'stock_code'와 '종목코드'가 일치하는 행만 추출
    merged_df = pd.merge(corp_df, compare_df, left_on="stock_code", right_on="종목코드")
    result_df = merged_df[["corp_code", "corp_name", "stock_code"]].sort_values(
        by="corp_name"
    )

    # 결과를 새로운 CSV 파일로 저장
    result_df.to_csv("listed_corps.csv", index=True)
    return result_df


def get_reports(public_companys_df):
    corp_names = list(public_companys_df["corp_name"])
    bsns_years = [
        "2022",
        "2023",
    ]  # (1) 사업연도(4자리) ※ 2015년 이후 부터 정보제공
    report_codes = ["11013", "11012", "11014", "11011"]
    fs_div = "CFS"  # CFS:연결재무제표, OFS:재무제표
    call_count = 0
    max_call_count = 19000
    start_word = "3S"
    start_index = corp_names.index(start_word)
    while call_count < max_call_count:
        for corp_name in corp_names[start_index:]:
            for bsns_year in bsns_years:
                for report_code in report_codes:
                    get_report(
                        public_companys_df, corp_name, bsns_year, report_code, fs_div
                    )
                    call_count += 1
        end_corp_name = corp_name
        print(end_corp_name)


set_api_key()
corps_df = get_corps_df()
listed_corps_df = remove_delisted_corps(corps_df)
get_reports(listed_corps_df)
