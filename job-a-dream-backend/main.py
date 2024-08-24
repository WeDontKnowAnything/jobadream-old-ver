from fastapi import FastAPI
from sqlalchemy import text
from database import models, connector
import uvicorn

from routers.corporations import router

models.Base.metadata.create_all(bind=connector.engine)

app = FastAPI()

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Welcome to jobAdream"}


# DB 연동 확인용 -> 확인 후 지울 것
@app.get("/db_name")
def get_database_name():
    with connector.engine.connect() as connection:
        result = connection.execute(text("SELECT current_database();"))
        db_name = result.scalar()  # 단일 값을 가져옵니다.
    return {"database_name": db_name}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
