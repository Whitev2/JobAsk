from re import search
from typing import Union, List

from fastapi import UploadFile
from sqlalchemy import update, delete, func, select, text

from database.postgres import Postgres
from news.models import News
from news.schemas import CreateNewsSchema, NewsResponse


class NewsClass:

    async def create(self, data: CreateNewsSchema, image: UploadFile = None):
        news = News(**data.dict())
        async with Postgres().get_session() as session:
            session.add(news)
            await session.commit()
            await session.refresh(news)

        return NewsResponse(**news.__dict__)

    async def get(self, id: int) -> Union[NewsResponse, None]:
        async with Postgres().get_session() as session:
            news = await session.get(News, id)

        return news

    async def view(self, id: int):
        news = await self.get(id)

        query = update(News).where(News.id == id).values(views=news.views + 1)

        async with Postgres().get_session() as session:
            await session.execute(query)
            await session.commit()

        return await self.get(id)

    async def like(self, id: int):
        news = await self.get(id)

        query = update(News).where(News.id == id).values(views=news.likes + 1)

        async with Postgres().get_session() as session:
            await session.execute(query)
            await session.commit()

        return await self.get(id)

    async def delete(self, id: int):
        async with Postgres().get_session() as session:
            await session.execute(delete(News).where(News.id == id))

        return {}

    async def all(self, page: int = 0, page_size: int = 15) -> List[NewsResponse]:
        query = select(News).order_by(News.updated_at)

        if page_size:
            query = query.limit(page_size)
        if page:
            query = query.offset(page * page_size)

        async with Postgres().get_session() as session:
            result = await session.execute(query)
            result = result.scalars()

        return [NewsResponse(**i.__dict__) for i in result]

    async def search(self, term) -> Union[None, List[NewsResponse]]:

        return None


news_crud = NewsClass()
