from pydantic import BaseModel

#Post Models

class Post(BaseModel):
    id = int
    title = str
    description = str

class PostCreate(Post):
    pass

class PostAll(BaseModel):
    id = int
    title = str
    description = str

class PostOne(Post):
    pass