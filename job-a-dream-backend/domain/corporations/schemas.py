from pydantic import BaseModel
from typing import List


# Corporation schema
class CorporationBase(BaseModel):
    id: str
    name: str


class Corporation(CorporationBase):
    category_code: str | None
    size_code: str | None
    employee_cnt: int | None
    reg_gender: int | None
    tempo_gender: int | None

    class Config:
        from_attributes = True


class Jobs(BaseModel):
    corp_name: str
    title: str | None
    category_code: str | None
    job_url: List | None

    class Config:
        from_attributes = True
