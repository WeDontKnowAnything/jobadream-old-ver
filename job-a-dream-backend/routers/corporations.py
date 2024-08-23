from sqlalchemy.orm import Session
from fastapi import APIRouter
from database.models import Corporation

router = APIRouter()


@router.get("/api/v1/corporations")
def read_all_corporations(db: Session, limit: int = 20):
    return db.query(Corporation).limit(limit).all()
