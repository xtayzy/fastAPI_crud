from sqlalchemy import select
from sqlalchemy.orm import joinedload

from datebase import async_session_maker
from posts.models import Post, Task
from repository.base import BaseRepository


class PostRepository(BaseRepository):
    model = Post


    # @classmethod
    # async def get_by_id(cls, pk):
    #     async with async_session_maker() as sessions:
    #         query = select(cls.model).filter_by(id=pk)
    #         result = await sessions.execute(query)
    #         result = result.scalar_one_or_none()
    #         if result is None:
    #             raise HTTPException(status_code=404, detail="obj not found")
    #         return result


class TaskRepository(BaseRepository):
    model = Task

