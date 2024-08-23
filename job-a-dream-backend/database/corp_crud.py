from sqlalchemy.orm import Session
from models import Corporation


def get_all_corporations(db: Session, limit: int = 20):
    return db.query(Corporation).limit(limit).all()


def get_corporation(db: Session, corp_id: str):
    return db.query(Corporation).filter(Corporation.corp_id.ilike(corp_id))
