from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from datebase import async_session_maker


class BaseRepository:
    model = None

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as sessions:
            query = select(cls.model)
            result = await sessions.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_by_id(cls, pk):
        async with async_session_maker() as sessions:
            query = select(cls.model).filter_by(id=pk)
            result = await sessions.execute(query)
            result = result.scalar_one_or_none()
            if result is None:
                raise HTTPException(status_code=404, detail="obj not found")
            return result

    @classmethod
    async def create(cls, data):
        async with async_session_maker() as sessions:
            query = cls.model(**data.dict())
            sessions.add(query)
            await sessions.commit()
            return query

    @classmethod
    async def update(cls, pk, **data):
        async with async_session_maker() as sessions:
            query = select(cls.model).filter_by(id=pk)
            result = await sessions.execute(query)
            result = result.scalar_one_or_none()
            if result is None:
                raise HTTPException(status_code=404, detail="obj not found")

            for key, value in data.items():
                setattr(result, key, value)

            await sessions.commit()

            return result

    @classmethod
    async def delete(cls, pk):
        async with async_session_maker() as sessions:
            query = select(cls.model).filter_by(id=pk)
            result = await sessions.execute(query)
            result = result.scalar_one_or_none()
            if result is None:
                raise HTTPException(status_code=404, detail="obj not found")

            await sessions.delete(result)
            await sessions.commit()

            return {
                "detail": "deleted"
            }
