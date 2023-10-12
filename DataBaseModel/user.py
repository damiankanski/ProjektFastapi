from typing import Dict, Union

from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


# Create user


def create_user(user: User, db: Session) -> User:
    newUser = User(id=user.id, name=user.name, password=user.password)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


# List of users


def get_all_users(db: Session):
    all_users = db.query(User).all()
    return all_users


# One user


def get_one_user(db: Session, name: str):
    one_user = db.query(User).filter(User.name == name).first()
    return one_user


# Modify user
def modify_user(db: Session, user_id: int, values: Dict[str, Union[str, int]]):
    user = db.query(User).filter(User.id == user_id).first()

    if user:
        for key, value in values.items():
            setattr(user, key, value)

        db.commit()
        return user.first()
    else:
        raise ValueError("User not found")


# Delete user
def delete_user(db: Session, user_id: str):
    deleted = db.query(User).filter(User.id == user_id)

    user = deleted.first()

    deleted.delete()
    db.commit()

    return user
