from sqlalchemy.orm import Session
from sqlalchemy import select
from domain.corporations.schemas import Corporation
from models import Corporation


def get_all_corporations(db: Session):
    result = db.execute(select(Corporation)).scalars().all()
    return result
