from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from connector import get_db
from domain.posts import crud, schemas
from typing import List

router = APIRouter()


@router.get("/api/v1/boards", response_model=List[schemas.PostResponse])
def read_posts(skip: int = 0, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip)
    return posts


@router.get("/api/v1/posts", response_model=schemas.PostResponse)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/api/v1/posts", response_model=schemas.PostResponse)
def create_new_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    try:
        created_post = crud.create_post(db=db, post=post)
        return created_post
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/api/v1/posts/comments", response_model=List[schemas.CommentResponse])
def read_comments(post_id: int, db: Session = Depends(get_db)):
    comments = crud.get_comments(db, post_id=post_id)
    if not comments:
        raise HTTPException(status_code=404, detail="Comments not found")
    return comments


@router.post("/api/v1/posts/comments", response_model=schemas.CommentResponse)
def create_new_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    new_comment = crud.create_comment(db=db, comment=comment)
    return new_comment
