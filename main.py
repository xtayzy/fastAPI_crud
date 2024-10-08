from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from posts.rep import PostRepository

app = FastAPI()


@app.get('/posts')
async def get_all_posts():
    posts = await PostRepository.get_all()
    return posts


@app.get('/posts/{post_id}')
async def get_post_by_id(post_id: int):
    post = await PostRepository.get_by_id(pk=post_id)
    return post


@app.delete('/posts/delete/{post_id}')
async def delete_post(post_id: int):
    post = await PostRepository.delete(pk=post_id)
    return post


class PostData(BaseModel):
    title: str
    description: str


@app.patch('/posts/update/{post_id}')
async def update_post(data: PostData, post_id: int):
    post = await PostRepository.update(pk=post_id, **data.dict())
    return post


@app.post('/posts')
async def post_post(data: PostData):
    return await PostRepository.create(data=data)
