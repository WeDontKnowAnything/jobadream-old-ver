from sqlalchemy.orm import Session
from models import Post, Comment
from domain.posts.schemas import PostCreate, CommentCreate
from datetime import datetime


def _build_post_response(post: Post, comments: list[Comment]):
    return {
        "title": post.title,
        "content": post.content,
        "post_id": post.id,
        "posting_date": post.posting_date,
        "view_count": post.view_count,
        "comments": [
            {
                "comment_id": comment.id,
                "post_id": comment.post_id,
                "comment": comment.comment,
                "comment_date": comment.comment_date,
            }
            for comment in comments
        ],
    }


def get_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return None

    # 조회수 증가
    post.view_count += 1
    db.commit()
    db.refresh(post)  # 변경된 내용을 반영

    comments = db.query(Comment).filter(Comment.post_id == post_id).all()
    return _build_post_response(post, comments)


def get_posts(db: Session):
    posts = db.query(Post).all()
    return [
        _build_post_response(
            post, db.query(Comment).filter(Comment.post_id == post.id).all()
        )
        for post in posts
    ]


def create_post(db: Session, post: PostCreate):
    db_post = Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_comments(db: Session, post_id: int):
    comments = db.query(Comment).filter(Comment.post_id == post_id).all()
    return [
        {
            "comment_id": comment.id,
            "post_id": comment.post_id,
            "comment": comment.comment,
            "comment_date": comment.comment_date,
        }
        for comment in comments
    ]


def create_comment(db: Session, comment: CommentCreate):
    db_comment = Comment(post_id=comment.post_id, comment=comment.comment)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return {
        "comment": db_comment.comment,
        "comment_id": db_comment.id,
        "post_id": db_comment.post_id,
        "comment_date": db_comment.comment_date,
    }
