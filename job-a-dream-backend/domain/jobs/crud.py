from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Jobs
from typing import List


def get_all_jobs(db: Session) -> List[dict]:
    jobs = db.execute(select(Jobs)).scalars().all()
    return jobs


def get_job(corp_id: str, db: Session) -> List[dict]:
    job = db.execute(select(Jobs).filter(Jobs.id == corp_id)).scalars().all()
    return job
