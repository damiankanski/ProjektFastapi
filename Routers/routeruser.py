from fastapi import APIRouter, Depends, HTTPException

from typing import List

from database import get_db
from DataBaseModel.user import User as dataUser
from DataBaseModel.user import (
    create_user,
    delete_user,
    get_all_users,
    get_one_user,
    modify_user,
)
from PydanticModel.user import User
from sqlalchemy.orm import Session
from starlette import status

router = APIRouter(tags=["User endpoints"])


# create user
@router.post("/v1/posts", status_code=status.HTTP_201_CREATED)
async def user_create(user: User, db: Session = Depends(get_db)) -> User:
    if user in dataUser:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"{user.name} already exist",
        )
    return create_user(user=user, db=db)


# get all users
@router.get("/v1/users", status_code=status.HTTP_200_OK)
async def user_list(db: Session = Depends(get_db)) -> List[User]:
    return get_all_users(db=db)


# get one user
@router.get("/v1/users/{name}", status_code=status.HTTP_200_OK)
async def user_name(name: str, db: Session = Depends(get_db)) -> User:
    if name not in dataUser:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"This {name} is not exist"
        )
    return get_one_user(name=name, db=db)


# modify_user
@router.patch("/v1/users/{user_id}", status_code=status.HTTP_200_OK)
async def user_update(user_id: int, db: Session = Depends(get_db)) -> User:
    if user_id not in dataUser:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user {user_id} is not exist",
        )
    return modify_user(user_id=user_id, db=db)


# delete user
@router.delete("/v1/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def user_delete(user_id: int, db: Session = Depends(get_db)) -> None:
    if user_id not in dataUser:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user {user_id} is not exist",
        )
    return delete_user(user_id=user_id, db=db)
