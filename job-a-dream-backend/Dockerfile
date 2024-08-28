# Backend Dockerfile
FROM python:3.12-slim

# PostgreSQL 클라이언트 라이브러리 설치
RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]