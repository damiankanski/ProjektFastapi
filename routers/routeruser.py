from fastapi import APIRouter

router = APIRouter(prefix="/User")

#create user
@router.post()

#get all users
@router.get()

#get one user
@router.get()

#modify_user
@router.patch()

#delete user
@router.delete()