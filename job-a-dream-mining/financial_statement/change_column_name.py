import os
from concurrent.futures import ProcessPoolExecutor, as_completed

import pandas as pd
from constants import Column, Path


def process_file(file_path):
    # CSV 파일 읽기
    df = pd.read_csv(file_path)

    # 칼럼명 변환
    df.rename(columns=Column.COLUMN_NAMES.value, inplace=True)

    # 변환된 CSV 파일 저장 (덮어쓰기)
    df.to_csv(file_path, index=False)


def create_file_path():
    file_paths = [
        os.path.join(Column.CSV2CHANGE_DIR.value, filename)
        for filename in os.listdir(Column.CSV2CHANGE_DIR.value)
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
