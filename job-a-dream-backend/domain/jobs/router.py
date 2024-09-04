from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from connector import get_db
from domain.jobs import crud, schemas
from typing import List

router = APIRouter()


@router.get("/api/v1/job/all", response_model=List[schemas.Jobs])
def read_all_jobs(db: Session = Depends(get_db)) -> List[dict]:
    try:
        jobs = crud.get_all_jobs(db)
        for job in jobs:
            job.job_url = crud.get_job_urls(job.id, db)
        return jobs
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/api/v1/job", response_model=schemas.JobsBase)
def read_job(job_id: str, db: Session = Depends(get_db)) -> List[dict]:
    try:
        job = crud.get_job(job_id, db)
        job.job_url = crud.get_job_urls(job_id, db)
        return job
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
