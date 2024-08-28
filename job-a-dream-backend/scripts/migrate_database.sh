#!/bin/bash
# 데이터베이스 마이그레이션
cd /app

# 만약 Alembic을 사용한다면 아래 명령을 사용합니다.
alembic upgrade head

# 또는 만약 SQL 파일로 직접 마이그레이션 한다면:
# psql -h <DB_HOST> -U <DB_USER> -d <DB_NAME> -f migrations/upgrade.sql