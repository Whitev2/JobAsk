import datetime
import json
from typing import Union

from pydantic import BaseModel


class CreateNewsSchema(BaseModel):
    title: str
    body: str

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class NewsResponse(BaseModel):
    id: int
    title: str
    body: str
    image_path: Union[None, str]
    likes: int
    views: int
