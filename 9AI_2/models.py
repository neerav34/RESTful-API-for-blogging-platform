from pydantic import BaseModel
from typing import List


class Comment(BaseModel):
    content: str


class LikeDislike(BaseModel):
    value: int


class Post(BaseModel):
    title: str
    content: str
    comments: List[Comment] = []
    likes: int = 0
    dislikes: int = 0
