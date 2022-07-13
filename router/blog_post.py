from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix='/blog', tags=['Blog'], )


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]


@router.post('/new', summary='post a blog')
def creat_blog(blog: BlogModel):
    return {'message': 'blog created', 'data': blog}
