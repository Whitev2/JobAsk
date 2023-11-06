from fastapi import Depends
from fastapi import HTTPException
from starlette import status

from app.auth.schemas import JwtSchema
from app.utils.oauth2 import JWTBearer, JwtHandler


async def user_data(token: str = Depends(JWTBearer())) -> JwtSchema:
    cred_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Credentials are not valid"
    )
    if token is None:
        raise cred_error

    # token_status = await DataRedis().get_data(token)

    # if token_status == 'blocked':
    #    raise cred_error

    payload = JwtHandler().decode_access_token(token)

    if payload is None:
        raise cred_error

    if payload.get("type") != "access":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")

    if payload.get("sgm") is True:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user_id = payload.get("sub", None)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user_hash = payload.get("hash", None)

    return JwtSchema(user_id=int(user_id), hash=user_hash)


async def anon_data(token: str = Depends(JWTBearer())) -> JwtSchema:
    cred_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Credentials are not valid"
    )

    payload = JwtHandler().decode_access_token(token)

    if payload is None:
        raise cred_error

    if payload.get("type") != "access":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")

    user_id = payload.get("sub", None)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user_hash = payload.get("hash", None)

    return JwtSchema(user_id=int(user_id), hash=user_hash)
