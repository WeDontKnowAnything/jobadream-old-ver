import uvicorn
from connector import Base, engine
from domain.corporations import router as corp_router
from domain.jobs import router as jobs_router
from domain.posts import router as posts_router
from domain.search import router as search_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
origins = [
    # "http://localhost:3000",
    "https://jobadream.com",
]  # Vue.js 개발 서버의 도메인

app = FastAPI()

app.include_router(corp_router.router)
app.include_router(jobs_router.router)
app.include_router(posts_router.router)
app.include_router(search_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 허용할 도메인 설정
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)


@app.get("/")
def root():
    return {"message": "Welcome to jobAdream"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
