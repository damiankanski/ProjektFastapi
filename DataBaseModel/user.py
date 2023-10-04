from database import base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Session
from typing import Dict, Union

class User(base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)



#stworz usera

def creat_user(user: User, db: Session) -> User:
    newUser = User(id=user.id, name=user.name, password=user.password)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


#zwroc wszytskich userow

def get_all_users(db: Session):
    all_users = db.query(User).all()
    return all_users

#zwroc dane usera

def get_one_user(db: Session, name: str):
    one_user = db.query(User).filter(User.name == name).first()
    return one_user

#modyfikuj usera
def modify_user(db: Session, user_id: int, values: Dict[str, Union[str, int]]):
    modifyUser = db.query(User).filter(User.id == user_id).first()

    if modifyUser :
        for key, value in values.items():
            setattr(modifyUser, key, value)

        db.commit()
        return modifyUser.first()
    else:
        raise ValueError("User not found")

#usun uzytkownika
def delete_user(db: Session, name: str):
    deleted = db.query(User).filter(User.name == name)

    user = deleted.first()

    deleted.delete()
    db.commit()

    return user

