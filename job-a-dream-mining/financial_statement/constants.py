from enum import Enum


class Path(Enum):
    CSV2COMPARE_FILE = "../data/listed_corps/상장법인목록_2024_08_09.csv"

    # 지정된 디렉토리 경로
    CSV2CHANGE_DIR = "../data/financial_reports"


class Report(Enum):
    BSNS_YEARS = [
        "2020",
    ]  # (1) 사업연도(4자리) ※ 2015년 이후 부터 정보제공
    REPORT_LIST = {
        "11013": "1분기",
        "11012": "반기",
        "11014": "3분기",
        "11011": "사업",
    }  # (3) 1분기보고서 : 11013 반기보고서 : 11012 3분기보고서 : 11014 사업보고서 : 11011
    FS_DIV = ["CFS", "OFS"]  # (4) CFS : 연결재무제표 OFS : 재무제표
    START_CORP_NAME = "케이티앤지"  # 시작할 기업명


class Column(Enum):
    # 변경할 칼럼명 딕셔너리
    COLUMN_NAMES = {
        "rcept_no": "접수번호",
        "reprt_code": "보고서 코드",
        "bsns_year": "사업 연도",
        "corp_code": "고유번호",
        "sj_div": "재무제표구분",
        "sj_nm": "재무제표명",
        "account_id": "계정ID",
        "account_nm": "계정명",
        "account_detail": "계정상세",
        "thstrm_nm": "당기명",
        "thstrm_amount": "당기금액",
        "thstrm_add_amount": "당기누적금액",
        "frmtrm_nm": "전기명",
        "frmtrm_amount": "전기금액",
        "frmtrm_q_nm": "전기명(분/반기)",
        "frmtrm_q_amount": "전기금액(분/반기)",
        "frmtrm_add_amount": "전기누적금액",
        "bfefrmtrm_nm": "전전기명",
        "bfefrmtrm_amount": "전전기금액",
        "ord": "계정과목 정렬순서",
        "currency": "통화 단위",
    }
