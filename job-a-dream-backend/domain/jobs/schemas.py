from pydantic import BaseModel
from datetime import date
from typing import List


# Corporation schema
class JobsBase(BaseModel):
    corp_name: str
    title: str | None
    position: str | None
    location: str
    experience_code: int | None
    job_url: list | None
    opening_date: date | None
    closing_date: date | None


class Jobs(JobsBase):
    id: str

    class Config:
        from_attributes = True


class JobUrl(BaseModel):
    saramin: str | None
    jobkorea: str | None
    open_data: str | None
    job_id: str
