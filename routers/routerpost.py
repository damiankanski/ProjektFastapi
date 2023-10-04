from fastapi import APIRouter

router = APIRouter(prefix="/Post")

#create post
@router.post()

#get all post
@router.get()

#get all post for direct user
@router.get()

#get post for post_id
@router.get()

#get_post for post_title
@router.get()

#modify_post
@router.patch()

#delete post
@router.delete()
