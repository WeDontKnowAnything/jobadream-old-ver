from fastapi import FastAPI
from sqlalchemy import text
import uvicorn

from domain.corporations import corp_router
from domain.jobs import jobs_router
from domain.posts import posts_router
from connector import engine

app = FastAPI()
app.include_router(corp_router.router)
app.include_router(jobs_router.router)
app.include_router(posts_router.router)


@app.get("/")
def root():
    return {"message": "Welcome to jobAdream"}


# DB 연동 확인용 -> 확인 후 지울 것
@app.get("/db_name")
def get_database_name():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT current_database();"))
        db_name = result.scalar()  # 단일 값을 가져옵니다.
    return {"database_name": db_name}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
