from typing import Dict
from typing import List
from typing import Union

from fastapi import APIRouter, UploadFile, File, Body
from fastapi import Depends

from news.crud import news_crud
from news.schemas import CreateNewsSchema, NewsResponse

router = APIRouter(tags=["News API"])


@router.post("/create", response_model=NewsResponse)
async def create_news(data: CreateNewsSchema = Body(...), image:  UploadFile = File(None)):
    return await news_crud.create(data=data, image=image)


@router.get("/", response_model=List[NewsResponse])
async def all_news(page: int = 0, page_size: int = 40):
    return await news_crud.all(page=page, page_size=page_size)


@router.post("/search", response_model=List[NewsResponse])
async def all_news(term: str):
    return await news_crud.search(term=term)
