import dart_fss
import pandas as pd
from env import settings


def set_api_key():
    api_key = settings.DART_API_KEY
    dart_fss.set_api_key(api_key=api_key)


# public_company = 상장 기업
# corp = 회사
def get_public_companys_df():
    all_corps = dart_fss.api.filings.get_corp_code()
    all_corps_df = pd.DataFrame(all_corps)
    public_companys_df = all_corps_df[all_corps_df["stock_code"].notnull()].reset_index(
        drop=True
    )
    return public_companys_df


def get_report(corp_df, corp_name, bsns_year, report_code, fs_div):
    # (1) corp_code : 기업코드
    corp_code = corp_df[corp_df["corp_name"] == corp_name].iloc[
        0, 0
    ]  # corp_df에서 corp_name에 해당하는 corp_code를 찾아 corp_code에 저장
    # (2) bsns_year : 사업연도(4자리)
    bsns_year = str(bsns_year)

    # (3) 1분기보고서 : 11013 반기보고서 : 11012 3분기보고서 : 11014 사업보고서 : 11011
    report_names = {
        "11013": "1분기",
        "11012": "2분기",
        "11014": "3분기",
        "11011": "4분기",
    }

    report_name = report_names[report_code]
    data = dart_fss.api.finance.fnltt_singl_acnt_all(
        corp_code, bsns_year, report_code, fs_div, api_key=None
    )["list"]
    financial_report = pd.DataFrame(data)
    financial_report.to_csv(
        f"test_data/{corp_name} {bsns_year}년 {report_name} 재무보고서.csv", index=True
    )

    return financial_report


def get_reports(public_companys_df):
    corp_names = list(public_companys_df["corp_name"])
    bsns_years = [
        "2022",
        "2023",
        "2024",
    ]  # (1) 사업연도(4자리) ※ 2015년 이후 부터 정보제공
    report_codes = ["11013", "11012", "11014", "11011"]
    fs_div = "CFS"  # CFS:연결재무제표, OFS:재무제표

    try:
        for corp_name in corp_names:
            for bsns_year in bsns_years:
                for reprt_code in report_codes:
                    # 만약 해당 사업연도, 분기에 해당하는 재무제표가 없다면
                    # 연결재무제표가 있으면 연결재무제표를, 없으면 재무제표를 가져온다.
                    financial_report = get_report(
                        public_companys_df, corp_name, bsns_year, reprt_code, fs_div
                    )
                    return financial_report
    except:
        # 해당 사업연도, 분기에 해당하는 재무제표가 없다면 다음 사업연도, 분기로 넘어간다.
        print(f"{bsns_year}년 {reprt_code}분기 재무제표가 없습니다.")
        pass


if __name__ == "__main__":
    set_api_key()
    public_companys_df = get_public_companys_df()
    financial_report = get_reports(public_companys_df)
