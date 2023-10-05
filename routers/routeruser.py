from fastapi import APIRouter, Depends, HTTPException
from typing import List
from PydenticModel.user import User
from starlette import status
from sqlalchemy.orm import Session
from database import get_db
from DataBaseModel.user import create_user, get_all_users, get_one_user, modify_user, delete_user
from DataBaseModel.user import User as dataUser
router = APIRouter(prefix="/User", tags="User endpoints")

#create user
@router.post("/createuser", status_code=status.HTTP_201_CREATED)
async def create_User(user: User,db: Session = Depends(get_db)) ->User:
    if user in dataUser:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail =f"{user.name} already exist")
    return create_user(user=user, db=db)



#get all users
@router.get("/allusers", status_code=status.HTTP_200_OK)
async def get_all_Users(db: Session = Depends(get_db)) -> List[User]:
    return get_all_users(db=db)

#get one user
@router.get("/oneuser", status_code=status.HTTP_200_OK)
async def get_one_User(name: str, db: Session = Depends(get_db)) -> User:
    return get_one_user(name=name, db=db)

#modify_user
@router.patch("/modify/user_id=user_id, db=db", status_code=status.HTTP_200_OK)
async def modify_User(user_id: int,db: Session = Depends(get_db)) -> User:
    return modify_user(user_id=user_id, db=db)

#delete user
@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_User(user_id: int,db: Session = Depends(get_db)) -> None:
    return delete_user(user_id=user_id, db=db)