from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from connector import get_db
from domain.search import crud, schemas
from typing import List, Annotated

router = APIRouter()


@router.get(
    "/api/v1/search/corporations",
    response_model=List[schemas.SearchCorporations],
)
def read_corporations(keyword: str, db: Session = Depends(get_db)):
    try:
        corporations = crud.get_corporations(keyword, db)
        return corporations
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/api/v1/search/jobs", response_model=List[schemas.SearchJobs])
def read_jobs(
    location: Annotated[list[str] | None, Query()] = None,
    position: Annotated[list[str] | None, Query()] = None,
    keyword: Annotated[list[str] | None, Query()] = None,
    db: Session = Depends(get_db),
):
    try:
        jobs = crud.get_jobs(location, position, keyword, db)
        for job in jobs:
            job.url = crud.get_job_urls(job.id, db)
        return jobs
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/api/v1/posts", response_model=List[schemas.SearchPosts])
def read_posts(keyword: str, db: Session = Depends(get_db)):
    try:
        posts = crud.get_posts(keyword, db)
        return posts
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
