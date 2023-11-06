from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import Form
from fastapi import HTTPException
from fastapi import status
from fastapi import UploadFile, Request

from auth.crud import Auth
from auth.current_user import anon_data
from auth.schemas import LoginSchema, JwtSchema, RefreshSchema, BaseMessageSchema, TokenSchema
from auth.oauth2 import jwt_h, JwtHandler

router = APIRouter(tags=["User Authentication"])


@router.post(
    "/register",
    status_code=201,
    responses={
        201: {"model": TokenSchema, "description": "Successfully login"},
        403: {"model": BaseMessageSchema, "description": "Invalid verification"},
        500: {"model": BaseMessageSchema, "description": "Server error"},
    },
)
async def login(request: Request, ):
    pass


@router.post(
    "/login",
    status_code=200,
    responses={
        200: {"model": TokenSchema, "description": "Successfully login"},
        403: {"model": BaseMessageSchema, "description": "Invalid verification"},
        404: {"model": BaseMessageSchema, "description": "User not found"},
        500: {"model": BaseMessageSchema, "description": "Server error"},
    },
)
async def login(request: Request,
                e: str = Form(...),
                last_name: str = Form(None)
                ):
    ip = request.client.host
    pass


@router.post(
    "/refresh",
    status_code=200,
    responses={
        200: {"model": TokenSchema, "description": "Successfully login"},
        401: {"model": BaseMessageSchema, "description": "Invalid refresh token"},
    },
)
async def refresh_token(data: RefreshSchema):
    jwt = JwtHandler()
    return await jwt.refresh(data)


@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout():
    pass
