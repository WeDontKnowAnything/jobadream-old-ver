from typing import List

from models import Corporation, Jobs, JobUrl
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_all_corporations(db: Session) -> List[dict]:
    corporations = db.execute(select(Corporation)).scalars().all()
    return corporations


def _get_corporation_job_urls(job_id: str, db: Session) -> List[dict]:
    job_urls = (
        db.execute(select(JobUrl).filter(JobUrl.job_id == job_id)).scalars().all()
    )

    result = [
        {"platform_name": job_url.platform_name, "url": job_url.url}
        for job_url in job_urls
    ]
    return result


def _get_corporation_jobs(corp_id: str, db: Session) -> List[dict]:
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

    jobs = [
        {
            "title": corporation_job.title,
            "position": corporation_job.position,
            "job_url": _get_corporation_job_urls(corporation_job.id, db),
        }
        for corporation_job in corporation_jobs
    ]
    return jobs


def get_corporation(corp_id: str, db: Session) -> List[dict]:
    corporation = (
        db.execute(select(Corporation).filter(Corporation.id == corp_id))
        .scalars()
        .first()
    )

    jobs = _get_corporation_jobs(corp_id, db)

    result = {"id": corporation.id, "name": corporation.name, "jobs": jobs}
    return result
