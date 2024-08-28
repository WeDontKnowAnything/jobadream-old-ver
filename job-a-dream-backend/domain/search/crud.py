from sqlalchemy.orm import Session
from sqlalchemy import select, or_
from models import Corporation, Jobs, JobUrl, Post
from typing import List


def get_corporations(keyword: str, db: Session) -> List[dict]:
    if keyword:
        search = "%%{}%%".format(keyword)
        corporations = (
            db.execute(select(Corporation).filter(Corporation.name.ilike(search)))
            .scalars()
            .all()
        )
    return corporations


def get_jobs(
    location: list[str | None] | None,
    position: list[str | None] | None,
    keyword: list[str | None] | None,
    db: Session,
):
    query = db.query(Jobs)
    if location is not None:
        query = query.filter(
            or_(
                *[
                    Jobs.location.ilike(f"%{loc}%")
                    for loc in location
                    if loc is not None
                ]
            )
        )
    if position is not None:
        query = query.filter(
            or_(
                *[
                    Jobs.category_code.ilike(f"%{po}%")
                    for po in position
                    if po is not None
                ]
            )
        )
    if keyword is not None:
        query = query.filter(
            or_(*[Jobs.title.ilike(f"%{key}%") for key in keyword if key is not None])
        )

    jobs = query.all()
    return jobs


def get_job_urls(job_id: str, db: Session) -> List[dict]:
    job_urls = (
        db.execute(select(JobUrl).filter(JobUrl.job_id == job_id)).scalars().all()
    )

    result = [
        {"platform_name": job_url.platform_name, "url": job_url.url}
        for job_url in job_urls
    ]
    return result


def get_posts(keyword: str, db: Session) -> List[dict]:
    if keyword:
        search = "%%{}%%".format(keyword)
        posts = (
            db.execute(select(Post).filter(Post.title.ilike(search))).scalars().all()
        )
    return posts
