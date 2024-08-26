from pydantic import BaseModel
from datetime import date


# Corporation schema
class JobsBase(BaseModel):
    corp_name: str
    title: str | None
    category_code: int | None
    location: str
    experience_code: int | None
    job_url: str | None
    opening_date: date | None
    closing_date: date | None


class Jobs(JobsBase):
    id: str

    class Config:
        from_attributes = True
