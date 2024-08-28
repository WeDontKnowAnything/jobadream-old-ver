#!/bin/bash
# 서버 시작
cd /app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload