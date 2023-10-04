from database import base
from sqlalchemy import Column,Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship
from user import User
from typing import Dict, Union


class Post(base):

    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship(User)



# Create a post
def create_post(post: Post, db: Session) -> Post:
    newPost = Post(id=post.id, title=post.title, description=post.description, user=post.user)

    db.add(newPost)
    db.commit()
    db.refresh(newPost)

    return newPost



# Get all post
def get_all_posts(db: Session):
    all_posts = db.query(Post).all()
    return all_posts


#wszystkie posty konkretnego uzytkownika

def get_all_user_post(db: Session, id: int):
    user_posts =db.query(Post).filter(Post.user_id == id).all()
    return user_posts

#wyszukaj konkretny post dla id_postu
def get_direct_id_post(id: int, db: Session):
    direct_id_post = db.query(Post).filter(Post.id == id)
    return direct_id_post


#Wyszukaj konkretny post po title

def get_title_post(title: str, db: Session):
    title_post = db.query(Post).filter(Post.title == title)
    return title_post

#modyfikacja postu
def modify_post(id:int, db: Session , values: Dict[str, Union[str, int]]):

    modifyPost = db.query(Post).filter(Post.id == id).first()

    if modifyPost:
        for key, value in values.items():
            setattr(modifyPost, key, value)

        db.commit()
        return modifyPost.first()
    else:
        raise ValueError("Postr not found.")


#usuniecie postu

def delete_post(id: int, db: Session, user: int):
    deleted = db.query(Post).filter(Post.id == id)

    post = deleted.first()

    deleted.delete()
    db.commit()

    return post