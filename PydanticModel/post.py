from pydantic import BaseModel
from PydanticModel.user import User

# Post Models


class Post(BaseModel):
    id: int
    title: str
    description: str


# Model with user data
class PostOpt(Post):
    user: User

    class Config:
        orm_mode = True
