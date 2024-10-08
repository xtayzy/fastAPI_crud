from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from posts.rep import PostRepository, TaskRepository

app = FastAPI()


class TaskData(BaseModel):
    title: str
    description: str
    completed: bool = False


@app.get('/tasks')
async def get_all_tasks():
    tasks = await TaskRepository.get_all()
    return tasks


@app.get('/tasks/{task_id}')
async def get_task(task_id: int):
    return await TaskRepository.get_by_id(task_id)


@app.post('/tasks')
async def create_task(data: TaskData):
    return await TaskRepository.create(data)


@app.patch('/tasks/{task_id}')
async def update_task(task_id: int, data: TaskData):
    return await TaskRepository.update(task_id, **data.dict())


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    return await TaskRepository.delete(task_id)

