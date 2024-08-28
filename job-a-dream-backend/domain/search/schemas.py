from pydantic import BaseModel
from typing import List
from datetime import datetime, date


class SearchCorporations(BaseModel):
    id: str
    name: str


class SearchJobs(BaseModel):
    id: str
    corp_name: str
    title: str | None
    position: str | None
    url: List | None
    opening_date: date | None
    closing_date: date | None

    class Config:
        from_attributes = True


class SearchPosts(BaseModel):
    id: int
    title: str
    posting_date: datetime
