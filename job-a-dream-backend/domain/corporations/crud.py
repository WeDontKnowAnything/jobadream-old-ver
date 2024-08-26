from sqlalchemy.orm import Session
from sqlalchemy import select
from domain.corporations.schemas import Corporation
from models import Corporation


def get_all_corporations(db: Session):
    result = db.execute(select(Corporation)).scalars().all()
    return result


def get_corporation(corp_id: str, db: Session):
    result = (
        db.execute(select(Corporation).filter(Corporation.corp_id == corp_id))
        .scalars()
        .all()
    )
    return result
