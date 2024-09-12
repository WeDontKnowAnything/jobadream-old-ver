import boto3
import itertools
from env.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME


class S3DirectoryCreator:
    def __init__(
        self,
        bucket_name,
        stocks_csv_path,
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
        self.stocks_csv_path = stocks_csv_path

    def create_directory(self, year, quarter):
        key = f"category=etl/data_status=raw_data/dataset=stocks_data_markets/year={year}/quarter={quarter}/"
        self.s3.put_object(Bucket=self.bucket_name, Key=key)
        print(f"Created directory: {key}")

    def create_all_directories(self, years, quarters):
        combinations = itertools.product(years, quarters)
        for year, quarter in combinations:
            self.create_directory(year, quarter)


if __name__ == "__main__":
    bucket_name = "job-a-dream"
    stocks_csv_path = "./stocks_data_markets.csv"

    years = ["2020", "2021", "2022", "2023", "2024"]
    quarters = ["Q1", "Q2", "Q3", "Q4"]

    s3_creator = S3DirectoryCreator(
        bucket_name,
        stocks_csv_path,
        AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY,
        REGION_NAME,
    )

    s3_creator.create_all_directories(years, quarters)
