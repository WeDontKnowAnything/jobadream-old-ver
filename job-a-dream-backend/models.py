from sqlalchemy import Column, INT, TIMESTAMP, VARCHAR, Text
from sqlalchemy.orm import relationship
from connector import Base


class Code(Base):
    __tablename__ = "code"

    code = Column(INT, primary_key=True, autoincrement=True)
    code_name = Column(VARCHAR, nullable=False)
    code_desc = Column(VARCHAR, nullable=False)
    code_group = Column(VARCHAR)


class Corporation(Base):
    __tablename__ = "corporation"

    corp_id = Column(VARCHAR, primary_key=True)
    corp_name = Column(VARCHAR, nullable=False)
    category_code = Column(VARCHAR)
    size_code = Column(VARCHAR)  # nullable=False
    employee_cnt = Column(INT)
    reg_gender = Column(INT)
    tempo_gender = Column(INT)


# class StartupIR(Base):
#     __tablename__ = "startup_ir"

#     ir_id = Column(INT, primary_key=True)
#     product = Column(VARCHAR)
#     corp_desc = Column(Text)
#     total_investment = Column(VARCHAR)
#     keyword = Column(VARCHAR)
#     ir_code = Column(INT)
#     corp_id = Column(VARCHAR, nullable=False)


# class News(Base):
#     __tablename__ = "news"

#     news_id = Column(INT, primary_key=True)
#     news_title = Column(VARCHAR, nullable=False)
#     news_summary = Column(Text, nullable=False)
#     news_url = Column(VARCHAR, nullable=False)
#     news_time = Column(TIMESTAMP)
#     corp_id = Column(VARCHAR, nullable=False)


# class Post(Base):
#     __tablename__ = "post"

#     post_id = Column(INT, primary_key=True)
#     title = Column(VARCHAR, nullable=False)
#     contents = Column(Text, nullable=False)
#     posting_date = Column(TIMESTAMP, nullable=False)

#     comments = relationship(
#         "Comment",
#         back_populates="post",
#         primaryjoin="Post.post_id == Comment.post_id",
#     )


# class Comment(Base):
#     __tablename__ = "comment"

#     comment_id = Column(INT, primary_key=True)
#     comment = Column(Text, nullable=False)
#     comment_date = Column(TIMESTAMP, nullable=False)
#     post_id = Column(INT, nullable=False)

#     post = relationship(
#         "Post",
#         back_populates="comments",
#         primaryjoin="Comment.post_id == Post.post_id",
#     )
