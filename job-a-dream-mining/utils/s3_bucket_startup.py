import boto3
import itertools
from env.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME


class S3DirectoryCreator:
    def __init__(
        self,
        bucket_name,
        startup_csv_path,
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
        self.startup_csv_path = startup_csv_path

    def upload_file(self):
        # 업로드할 파일의 S3 내 경로
        key = f"category=etl/data_status=raw_data/dataset=startup/{self.startup_csv_path.split('/')[-1]}"

        # 파일 업로드
        try:
            self.s3.upload_file(self.startup_csv_path, self.bucket_name, key)
            print(f"File uploaded successfully to {key}")
        except Exception as e:
            print(f"Error uploading file: {e}")


if __name__ == "__main__":
    bucket_name = "job-a-dream"
    startup_csv_path = "./job-a-dream-mining/data/Startup_Data_20240816.csv"

    s3_creator = S3DirectoryCreator(
        bucket_name,
        startup_csv_path,
        AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY,
        REGION_NAME,
    )

    s3_creator.upload_file()
