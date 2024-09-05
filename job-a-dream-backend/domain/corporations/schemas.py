from pydantic import BaseModel
from typing import List


# Corporation schema
class CorporationBase(BaseModel):
    id: str
    name: str


class JobBase(BaseModel):
    title: str | None
    position: str | None
    job_url: List | None

    class Config:
        from_attributes = True


class Corporation(CorporationBase):
    jobs: List[JobBase] = []

    class Config:
        from_attributes = True


# class Corporation(CorporationBase):
#     category_code: int | None
#     size_code: str | None
#     employee_cnt: int | None
#     reg_gender: int | None
#     tempo_gender: int | None

#     class Config:
#         from_attributes = True
