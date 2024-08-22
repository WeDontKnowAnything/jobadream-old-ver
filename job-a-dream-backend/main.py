from fastapi import FastAPI
from database.connector import engine
from sqlalchemy import text

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to jobAdream"}


# DB 연동 확인
@app.get("/db_name")
def get_database_name():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT current_database();"))
        db_name = result.scalar()  # 단일 값을 가져옵니다.
    return {"database_name": db_name}
