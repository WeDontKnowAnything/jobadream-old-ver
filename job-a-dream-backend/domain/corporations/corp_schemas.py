from typing import List, Union
from pydantic import BaseModel


# Code schema
class CodeBase(BaseModel):
    code_name: str
    code_desc: str
    code_group: str


class Code(CodeBase):
    code: int

    class Config:
        from_attributes = True


# Corporation schema
class CorporationBase(BaseModel):
    corp_id: str
    corp_name: str


class Corporation(CorporationBase):
    # category_code: str
    # size_code: str
    # employee_cnt: int
    # reg_gender: int
    # tempo_gender: int
    pass

    class Config:
        from_attributes = True
