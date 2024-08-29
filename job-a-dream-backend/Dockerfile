# Backend Dockerfile
FROM python:3.12-slim

# PostgreSQL 클라이언트 라이브러리 설치
RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app

# 필요한 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 모든 소스 코드 복사
COPY . .

# 컨테이너 실행 시 Uvicorn을 사용하여 FastAPI 애플리케이션 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]