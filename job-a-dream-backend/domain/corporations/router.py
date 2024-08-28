from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from connector import get_db
from domain.corporations import crud, schemas
from typing import List

router = APIRouter()


@router.get("/api/v1/corporations", response_model=List[schemas.CorporationBase])
def read_all_corporations(db: Session = Depends(get_db)) -> List[dict]:
    try:
        corporations = crud.get_all_corporations(db)
        return corporations
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get(
    "/api/v1/corporations/{corp_id}", response_model=List[schemas.CorporationBase]
)
def read_corporation(corp_id: str, db: Session = Depends(get_db)) -> List[dict]:
    try:
        corporation = crud.get_corporation(corp_id, db)
        return corporation
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get(
    "/api/v1/corporations/{corp_id}/jobs", response_model=List[schemas.CorporationJobs]
)
def read_corporation_jobs(corp_id: str, db: Session = Depends(get_db)) -> List[dict]:
    try:
        corporation_jobs = crud.get_corporation_jobs(corp_id, db)
        return corporation_jobs
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
