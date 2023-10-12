from typing import Dict, Union

from database import Base
from DataBaseModel.user import User
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Session, relationship


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship(User)


# Create a post
def create_post(post: Post, db: Session, user: int) -> Post:
    newPost = Post(
        id=post.id, title=post.title, description=post.description, user_id=user
    )

    db.add(newPost)
    db.commit()
    db.refresh(newPost)

    return newPost


# Get all post
def get_all_posts(db: Session):
    all_posts = db.query(Post).all()
    return all_posts


# All posts for direct user


def get_all_user_post(id: int, db: Session):
    user_posts = db.query(Post).filter(Post.user_id == id).all()
    return user_posts


# Post for direct post id
def get_direct_id_post(user: int, id: int, db: Session):
    direct_id_post = db.query(Post).filter(Post.user_id == user, Post.id == id)
    return direct_id_post


# Post for title


def get_title_post(user: int, title: str, db: Session):
    title_post = db.query(Post).filter(Post.user_id == user, Post.title == title)
    return title_post


# Modify post
def modify_post(user: int, id: int, db: Session, values: Dict[str, Union[str, int]]):
    post = db.query(Post).filter(Post.user_id == user, Post.id == id).first()

    if post:
        for key, value in values.items():
            setattr(post, key, value)

        db.commit()
        return post.first()
    else:
        raise ValueError("Post not found.")


# Delete post


def delete_post(
    user: int,
    id: int,
    db: Session,
):
    deleted = db.query(Post).filter(Post.user_id == user, Post.id == id)

    post = deleted.first()

    deleted.delete()
    db.commit()

    return post
