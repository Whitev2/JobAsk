from typing import Dict
from typing import List
from typing import Union

from fastapi import APIRouter
from fastapi import Depends



router = APIRouter(tags=["User API"])


@router.get()
async def get_user(user: JwtSchema = Depends(user_data)):
    pass