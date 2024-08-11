import os
from concurrent.futures import ProcessPoolExecutor, as_completed

import pandas as pd

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

# 지정된 디렉토리 경로
directory = "../data/financial_reports"


def process_file(file_path):
    # CSV 파일 읽기
    df = pd.read_csv(file_path)

    # 칼럼명 변환
    df.rename(columns=COLUMN_NAMES, inplace=True)

    # 변환된 CSV 파일 저장 (덮어쓰기)
    df.to_csv(file_path, index=False)


def create_file_path():
    file_paths = [
        os.path.join(directory, filename)
        for filename in os.listdir(directory)
        # if filename.endswith(".csv")
    ]
    return file_paths


def process_files(file_paths):
    # 병렬 처리를 위한 ProcessPoolExecutor 설정
    with ProcessPoolExecutor() as executor:
        # 비동기적으로 파일 처리
        futures = [executor.submit(process_file, file_path) for file_path in file_paths]

        # 작업 완료 대기 및 결과 확인
        for future in as_completed(futures):
            # future.result()로 예외를 확인할 수 있음
            future.result()
    print("모든 파일이 처리되었습니다.")


def main():
    # 파일 경로 목록 생성
    file_paths = create_file_path()

    process_files(file_paths)


if __name__ == "__main__":
    main()
