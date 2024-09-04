import boto3
import itertools
import csv
from env.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME


class S3DirectoryCreator:
    def __init__(
        self,
        bucket_name,
        corporations_csv_path,
        aws_access_key_id,
        aws_secret_access_key,
        region_name,
    ):
        # AWS 자격 증명 및 region 설정
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )
        self.bucket_name = bucket_name
        self.corporations_csv_path = corporations_csv_path
        self.corporations = self.load_corporations()

    def load_corporations(self):
        corporations = []
        with open(self.corporations_csv_path, mode="r", encoding="utf-8-sig") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # 헤더 skip
            for row in csv_reader:
                corporations.append(row[2])  # 기업 이름 -> 2번 index
        return corporations

    def create_directory(self, corporation, year, quarter, statement_type):
        key = f"etl/raw_data/corporation_name={corporation}/year={year}/quarter={quarter}/statement_type={statement_type}/"
        self.s3.put_object(Bucket=self.bucket_name, Key=key)
        print(f"Created directory: {key}")

    def create_all_directories(self, years, quarters, statement_types):
        combinations = itertools.product(
            self.corporations, years, quarters, statement_types
        )
        for corporation, year, quarter, statement_type in combinations:
            self.create_directory(corporation, year, quarter, statement_type)


if __name__ == "__main__":
    bucket_name = "job-a-dream"
    corporations_csv_path = "./listed_corps.csv"

    years = ["2020", "2021", "2022", "2023", "2024"]
    quarters = ["Q1", "Q2", "Q3", "Q4"]
    statement_types = [
        "balance_sheet",  # 재무상태표
        "income_statement",  # 포괄손익계산서
        "cash_flow_statement",  # 현금흐름표
        "equity_changes_statement",  # 자본변동표
    ]

    s3_creator = S3DirectoryCreator(
        bucket_name,
        corporations_csv_path,
        AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY,
        REGION_NAME,
    )

    s3_creator.create_all_directories(years, quarters, statement_types)
