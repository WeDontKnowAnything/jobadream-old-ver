import dart_fss
import pandas as pd
from env import settings

from .constants import Path, Report


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


# 상폐 기업 제거 함수
def remove_delisted_corps(corp_df) -> pd.DataFrame:
    # CSV 파일 읽기

    compare_df = pd.read_csv(Path.CSV2COMPARE_FILE.value)

    # 데이터 타입 변환
    corp_df["stock_code"] = corp_df["stock_code"].astype(int)
    compare_df["종목코드"] = compare_df["종목코드"].astype(int)

    # 'stock_code'와 '종목코드'가 일치하는 행만 추출
    merged_df = pd.merge(corp_df, compare_df, left_on="stock_code", right_on="종목코드")
    result_df = merged_df[["corp_code", "corp_name", "stock_code"]].sort_values(
        by="corp_name"
    )

    # 결과를 새로운 CSV 파일로 저장
    # result_df.to_csv("listed_corps.csv", index=True)
    return result_df


def get_report(corp_df, corp_name, bsns_year, report_code):
    # (1) corp_code : 기업코드
    corp_code = corp_df[corp_df["corp_name"] == corp_name].iloc[
        0, 0
    ]  # corp_df에서 corp_name에 해당하는 corp_code를 찾아 corp_code에 저장

    report_name = Report.REPORT_LIST.value.get(report_code)

    # 만약 연결제무제표가 없다면 재무제표로 다시 시도
    try:
        data = dart_fss.api.finance.fnltt_singl_acnt_all(
            corp_code, bsns_year, report_code, Report.FS_DIV.value[0], api_key=None
        )["list"]
    except:
        try:
            data = dart_fss.api.finance.fnltt_singl_acnt_all(
                corp_code,
                bsns_year,
                report_code,
                Report.FS_DIV.value[1],
                api_key=None,
            )["list"]
        except:
            # 해당 사업연도, 분기에 해당하는 재무제표가 없다면 다음 사업연도, 분기로 넘어간다.
            # print(f"{corp_name}사의 {bsns_year}년 {report_name} 재무제표가 없습니다.")
            pass
        else:
            financial_report_df = pd.DataFrame(data)
            financial_report_df.to_csv(
                f"../data/financial_reports/{corp_name} {bsns_year}년 {report_name} 재무보고서.csv",
                index=True,
                encoding="utf-8-sig",
            )
    else:
        financial_report_df = pd.DataFrame(data)
        financial_report_df.to_csv(
            f"../data/financial_reports/{corp_name} {bsns_year}년 {report_name} 연결재무보고서.csv",
            index=True,
        )


def get_reports(public_companys_df):
    corp_names = list(public_companys_df["corp_name"])
    report_codes = list(Report.REPORT_LIST.value.keys())
    call_count = 0
    start_index = corp_names.index(Report.START_CORP_NAME.value)
    for corp_name in corp_names[start_index:]:
        for bsns_year in Report.BSNS_YEARS.value:
            for report_code in report_codes:
                get_report(public_companys_df, corp_name, bsns_year, report_code)
                call_count += 1
        print(f"{corp_name}사의 재무제표 수집 완료, api호출 수 : {call_count}")


def main():
    set_api_key()
    corps_df = get_corps_df()
    listed_corps_df = remove_delisted_corps(corps_df)
    get_reports(listed_corps_df)


if __name__ == "__main__":
    main()
