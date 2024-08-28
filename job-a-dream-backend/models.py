from sqlalchemy import Column, INT, TIMESTAMP, VARCHAR, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from connector import Base


class Code(Base):
    __tablename__ = "code"

    code = Column(INT, primary_key=True, autoincrement=True)
    code_name = Column(VARCHAR, nullable=False)
    code_desc = Column(VARCHAR, nullable=False)
    code_group = Column(VARCHAR)


class Corporation(Base):
    __tablename__ = "corporation"

    id = Column(VARCHAR, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    category_code = Column(VARCHAR)
    size_code = Column(VARCHAR)
    employee_cnt = Column(INT)
    reg_gender = Column(INT)
    tempo_gender = Column(INT)


class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(VARCHAR, primary_key=True)
    corp_name = Column(VARCHAR, nullable=False)
    title = Column(VARCHAR)
    category_code = Column(INT)
    location = Column(VARCHAR, nullable=False)
    experience_code = Column(INT)
    opening_date = Column(Date)
    closing_date = Column(Date)


class JobUrl(Base):
    __tablename__ = "job_url"

    id = Column(INT, primary_key=True, autoincrement=True)
    platform_name = Column(VARCHAR, nullable=False)
    url = Column(VARCHAR, nullable=False)
    job_id = Column(VARCHAR, nullable=False)


class StartupIR(Base):
    __tablename__ = "startup_ir"

    id = Column(INT, primary_key=True, autoincrement=True)
    product = Column(VARCHAR)
    corp_desc = Column(Text)
    total_investment = Column(VARCHAR)
    keyword = Column(VARCHAR)
    ir_code = Column(INT)
    startup_id = Column(VARCHAR, nullable=False)


class News(Base):
    __tablename__ = "news"

    id = Column(INT, primary_key=True, autoincrement=True)
    news_title = Column(VARCHAR, nullable=False)
    news_summary = Column(Text, nullable=False)
    news_url = Column(VARCHAR, nullable=False)
    news_time = Column(TIMESTAMP, nullable=False)
    corp_id = Column(VARCHAR, nullable=False)


class Post(Base):
    __tablename__ = "post"

    id = Column(INT, primary_key=True, autoincrement=True)
    title = Column(VARCHAR, nullable=False)
    content = Column(Text, nullable=False)
    posting_date = Column(TIMESTAMP, nullable=False, server_default=func.now())


class Comment(Base):
    __tablename__ = "comment"

    id = Column(INT, primary_key=True, autoincrement=True)
    comment = Column(Text, nullable=False)
    comment_date = Column(TIMESTAMP, nullable=False, server_default=func.now())
    post_id = Column(INT, ForeignKey("post.id"), nullable=False)
