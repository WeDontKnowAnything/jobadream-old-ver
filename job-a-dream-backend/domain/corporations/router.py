from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from connector import get_db
from domain.corporations import crud, schemas
from typing import List

router = APIRouter()


@router.get("/api/v1/corporations", response_model=List[schemas.Corporation])
def read_all_corporations(db: Session = Depends(get_db)):
    try:
        corporations = crud.get_all_corporations(db)
        return corporations
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
