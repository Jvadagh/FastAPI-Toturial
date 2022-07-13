from fastapi import APIRouter

router = APIRouter(prefix='/blog', tags=['Blog'], )


@router.post('/new', summary='post a blog')
def creat_blog():
    return {'message': 'blog created'}
