from typing import List, Union
from pydantic import BaseModel


# Corporation schema
class CorporationBase(BaseModel):
    corp_id: str
    corp_name: str


class Corporation(CorporationBase):
    category_code: str
    size_code: str
    employee_cnt: int
    reg_gender: int
    tempo_gender: int

    class Config:
        from_attributes = True
