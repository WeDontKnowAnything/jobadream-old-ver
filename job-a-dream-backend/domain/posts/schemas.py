from pydantic import BaseModel
from datetime import datetime
from typing import List


class CommentBase(BaseModel):
    comment: str


class CommentCreate(CommentBase):
    post_id: int


class CommentResponse(CommentBase):
    comment_id: int
    comment_date: datetime | None

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    post_id: int
    posting_date: datetime | None
    comments: List[CommentResponse] = []
    view_count: int

    class Config:
        from_attributes = True
