import boto3
import itertools
from env.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME
import csv

# AWS 자격 증명 및 리전 설정
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME,
)

# S3 버킷 이름
bucket_name = "job-a-dream"

# 기업 리스트
companies = ["CompanyA", "CompanyB", "CompanyC"]

# 디렉토리 구조 설정
years = ["2020", "2021", "2022", "2023", "2024"]
quarters = ["Q1", "Q2", "Q3", "Q4"]
statement_types = [
    "balance_sheet",  # 재무상태표
    "income_statement",  # 포괄손익계산서
    "cash_flow_statement",  # 현금흐름표
    "equity_changes_statement",  # 자본변동표
]

# 모든 조합 생성
combinations = itertools.product(companies, years, quarters, statement_types)

# 조합별 디렉토리 생성
for company, year, quarter, statement_type in combinations:
    # S3 디렉토리 경로 생성 (이후 '전처리 후', '최종 DB 저장용' 디렉토리 따로 설정)
    key = f"etl/raw_data//company_name={company}/year={year}/quarter={quarter}/statement_type={statement_type}/"

    # 빈 객체 업로드로 디렉토리 생성
    s3.put_object(Bucket=bucket_name, Key=key)

    print(f"Created directory: {key}")
