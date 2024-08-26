from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from connector import get_db
from domain.jobs import crud, schemas
from typing import List

router = APIRouter()


@router.get("/api/v1/jobs", response_model=List[schemas.Jobs])
def read_all_corporations(db: Session = Depends(get_db)) -> List[dict]:
    try:
        jobs = crud.get_all_jobs(db)
        return jobs
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/api/v1/jobs/{job_id}", response_model=List[schemas.JobsBase])
def read_corporation(job_id: str, db: Session = Depends(get_db)) -> List[dict]:
    try:
        job = crud.get_job(job_id, db)
        return job
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
