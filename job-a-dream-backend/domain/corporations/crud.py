from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Corporation, Jobs, JobUrl
from typing import List


def get_all_corporations(db: Session) -> List[dict]:
    corporations = db.execute(select(Corporation)).scalars().all()
    return corporations


def get_corporation(corp_id: str, db: Session) -> List[dict]:
    corporation = (
        db.execute(select(Corporation).filter(Corporation.id == corp_id))
        .scalars()
        .all()
    )
    return corporation


def get_corporation_jobs(corp_id: str, db: Session) -> List[dict]:
    corporation_name = (
        db.execute(select(Corporation.name).filter(Corporation.id == corp_id))
        .scalars()
        .first()
    )

    corporation_jobs = (
        db.execute(select(Jobs).filter(Jobs.corp_name == corporation_name))
        .scalars()
        .all()
    )
    return corporation_jobs


def get_corporation_job_urls(job_id: str, db: Session) -> List[dict]:
    job_urls = (
        db.execute(select(JobUrl).filter(JobUrl.job_id == job_id)).scalars().all()
    )

    result = [
        {"platform_name": job_url.platform_name, "url": job_url.url}
        for job_url in job_urls
    ]
    return result
