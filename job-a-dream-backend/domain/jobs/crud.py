from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Jobs, JobUrl
from typing import List


def get_all_jobs(db: Session) -> List[dict]:
    jobs = db.execute(select(Jobs)).scalars().all()
    return jobs


def get_job(job_id: str, db: Session) -> List[dict]:
    job = db.execute(select(Jobs).filter(Jobs.id == job_id)).scalars().first()
    return job


def get_job_urls(job_id: str, db: Session) -> List[dict]:
    job_urls = (
        db.execute(select(JobUrl).filter(JobUrl.job_id == job_id)).scalars().all()
    )

    result = [
        {"platform_name": job_url.platform_name, "url": job_url.url}
        for job_url in job_urls
    ]
    return result
