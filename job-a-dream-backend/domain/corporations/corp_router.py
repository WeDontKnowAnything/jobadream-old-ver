from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from connector import get_db
from domain.corporations import corp_crud, corp_schemas
from typing import List

router = APIRouter()


@router.get("/api/v1/corporations", response_model=List[corp_schemas.Corporation])
def read_all_corporations(db: Session = Depends(get_db)):
    try:
        corporations = corp_crud.get_all_corporations(db)
        return corporations
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
