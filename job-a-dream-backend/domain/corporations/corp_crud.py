from sqlalchemy.orm import Session
from database.models import Corporation


def get_all_corporations(db: Session, limit: int = 20):
    return db.query(Corporation).limit(limit).all()
