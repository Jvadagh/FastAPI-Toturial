from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional

router = APIRouter(prefix='/blog', tags=['Blog'])


class TypeBlogs(str, Enum):
    type1 = 'int'
    type2 = 'float'


@router.get('/{id}/comments/{comment_id}', tags=['comments'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog id :{id} comment id :{comment_id} {valid=} {username=}'}


@router.get('/all')
def get_blogs(page: int = 5, page_size: float = 200.00, ):
    return {'message': f"{page=} -- {page_size=}"}


@router.get('/type/{type}')
def get_type_blog(type: TypeBlogs):
    return {'message ': f'blog type is {type}'}

    # @app.get('/blogs/all')
    # def get_blogs():
    #     return {'message': f"all Blogs "}


@router.get('/{id}', status_code=status.HTTP_200_OK, summary='receive an ID',
            description='this API for receive ID of the blogs')
def get_blog(id: int, response: Response):
    if id > 10:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'Error': f'id {id} not valid'}
    return {'message': f"Blog = {id}"}
