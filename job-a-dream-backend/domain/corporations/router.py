from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from connector import get_db
from domain.corporations import crud, schemas
from typing import List

router = APIRouter()


@router.get("/api/v1/corporations", response_model=List[schemas.CorporationBase])
def read_all_corporations(
    skip: int = 0, limit: int = 12, db: Session = Depends(get_db)
) -> List[dict]:
    try:
        corporations = crud.get_all_corporations(skip, limit, db)
        return corporations
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/api/v1/corporation", response_model=List[schemas.CorporationBase])
def read_corporation(corp_id: str, db: Session = Depends(get_db)) -> List[dict]:
    try:
        corporation = crud.get_corporation(corp_id, db)
        return corporation
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/api/v1/corporations/jobs", response_model=List[schemas.Jobs])
def read_corporation_jobs(
    corp_id: str, skip: int = 0, limit: int = 12, db: Session = Depends(get_db)
) -> List[dict]:
    try:
        corporation_jobs = crud.get_corporation_jobs(corp_id, skip, limit, db)

        result = [
            {
                "corp_name": corporation_job.corp_name,
                "title": corporation_job.title,
                "category_code": corporation_job.category_code,
                "job_url": crud.get_corporation_job_urls(
                    corporation_job.id, skip, limit, db
                ),
            }
            for corporation_job in corporation_jobs
        ]

        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
