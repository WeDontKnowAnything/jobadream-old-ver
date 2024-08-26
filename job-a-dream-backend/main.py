from fastapi import FastAPI
import uvicorn

from domain.corporations import router as corp_router
from domain.jobs import router as jobs_router
from domain.posts import router as posts_router
from connector import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(corp_router.router)
app.include_router(jobs_router.router)
app.include_router(posts_router.router)


@app.get("/")
def root():
    return {"message": "Welcome to jobAdream"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
