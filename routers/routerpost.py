from fastapi import APIRouter, Depends, HTTPException

from typing import List

from database import get_db
from DataBaseModel.post import Post as dataPost
from DataBaseModel.post import (
    create_post,
    delete_post,
    get_all_posts,
    get_all_user_post,
    get_direct_id_post,
    get_title_post,
    modify_post,
)
from PydanticModel.post import Post, PostOpt
from sqlalchemy.orm import Session
from starlette import status

router = APIRouter(tags=["Post endpoints"])


# create post
@router.post("/v1/add-post", status_code=status.HTTP_201_CREATED)
async def post_create(
    post: Post, user: int, db: Session = Depends(get_db)
) -> List[PostOpt]:
    return create_post(post=post, user=user, db=db)


# get all post
@router.get("/v1/posts", status_code=status.HTTP_200_OK)
async def post_list(db: Session = Depends(get_db)) -> List[Post]:
    return get_all_posts(db=db)


# get all post for direct user
@router.get("/v1/posts/{user_id}", status_code=status.HTTP_200_OK)
async def post_by_user(
    user_id: int,
    db: Session = Depends(get_db),
) -> List[PostOpt]:
    if user_id not in dataPost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user {user_id} is not exist",
        )
    return get_all_user_post(id=user_id, db=db)


# get post for post_id
@router.get("/v1/posts/{user_id}/{post_id}", status_code=status.HTTP_200_OK)
async def post_by_id(
    user_id: int, post_id: int, db: Session = Depends(get_db)
) -> PostOpt:
    if user_id not in dataPost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user {user_id} is not exist",
        )
    elif post_id not in dataPost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The post {post_id} is not exist",
        )
    else:
        return get_direct_id_post(user=user_id, id=post_id, db=db)


# get_post for post_title
@router.get("/v1/posts/{title}", status_code=status.HTTP_200_OK)
async def post_title(title: str, db: Session = Depends(get_db)) -> Post:
    if title not in dataPost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with title- {title} is not exist",
        )
    return get_title_post(title=title, db=db)


# modify_post
@router.patch("/v1/posts/{user_id}/{post_id}", status_code=status.HTTP_200_OK)
async def post_update(
    user_id: int,
    post_id: int,
    db: Session = Depends(get_db),
) -> PostOpt:
    if user_id not in dataPost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user {user_id} is not exist",
        )
    elif post_id not in dataPost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The post {post_id} is not exist",
        )
    else:
        return modify_post(user=user_id, id=post_id, db=db)


# delete post
@router.delete("/v1/posts/{user_id}/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def post_delete(
    user_id: int, post_id: int, db: Session = Depends(get_db)
) -> None:
    if user_id not in dataPost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user {user_id} is not exist",
        )
    elif post_id not in dataPost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The post {post_id} is not exist",
        )
    else:
        return delete_post(user=user_id, id=post_id, db=db)
