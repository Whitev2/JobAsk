from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import declarative_base, sessionmaker
from contextlib import asynccontextmanager

from config import config

Base = declarative_base()


class Postgres:
    engine: AsyncEngine

    @classmethod
    async def connect_to_storage(cls):
        POSTGRES_URL = f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@db:5432/{config.POSTGRES_DB}"

        cls.engine = create_async_engine(POSTGRES_URL, echo=False)


    @classmethod
    def async_session_generator(cls):
        return sessionmaker(
            cls.engine, class_=AsyncSession
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncSession:
        try:
            async_session = self.async_session_generator()

            async with async_session() as session:
                yield session
        finally:
            print("СЕССИЯ ЗАКРЫЛАСЬ!!!!")
            await session.close()
