from typing import Union

from pydantic import BaseModel, EmailStr


class BaseMessageSchema(BaseModel):
    message: str


class RegisterSchema(BaseModel):
    email: EmailStr
    password: str
    username: str


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class TokenSchema(BaseModel):
    refresh_token: Union[str, None]
    access_token: str
    access_time: int
    refresh_time: int
    token_type: str = "Bearer"
    is_registered: bool


class JwtSchema(BaseModel):
    user_id: int
    hash: str


class RefreshSchema(BaseModel):
    refresh_token: str
