from datetime import datetime
from datetime import timedelta


from fastapi import HTTPException
from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from jose import jwt
from starlette import status

from config import config

from auth.schemas import TokenSchema, RefreshSchema


class JwtHandler:
    @classmethod
    def create_access_token(cls, uid: str, user_hash: str, exp_time: int = 0, security_mode: bool = False) -> str:
        """
        This function allows you to create a jwt token based on data
        uid: user_id

        """

        now = datetime.utcnow()

        payload = {
            "iat": now,
            "nbf": now,
            "exp": now + timedelta(minutes=exp_time),
            "sub": str(uid),
            "sgm": security_mode,
            "hash": user_hash,
            "type": "access",
        }
        token = jwt.encode(payload, config.SECRET_ACCESS_KEY, algorithm=config.JWT_ALGORITHM)
        return token

    @classmethod
    def create_refresh_token(cls, uid: str, user_hash: str, exp_time: int = 0, security_mode: bool = False) -> str:
        """
        This function allows you to create a jwt token based on data
        uid: user_id
        data: data dictionary
        """

        now = datetime.utcnow()

        payload = {
            "iat": now,
            "nbf": now,
            "exp": now + timedelta(minutes=exp_time),
            "sub": str(uid),
            "sgm": security_mode,
            "hash": user_hash,
            "type": "refresh",
        }
        token = jwt.encode(payload, config.SECRET_REFRESH_KEY, algorithm=config.JWT_ALGORITHM)
        return token

    @classmethod
    def decode_access_token(cls, token: str):
        """
        This function decrypts a jwt token
        token: jwt
        """
        try:
            encoded_jwt = jwt.decode(token, config.SECRET_ACCESS_KEY, config.JWT_ALGORITHM)
            return encoded_jwt
        except jwt.JWTError as e:
            print(e)
            return None

    @classmethod
    def decode_refresh_token(cls, token: str):
        """
        This function decrypts a jwt token
        token: jwt
        """
        try:
            encoded_jwt = jwt.decode(token, config.SECRET_REFRESH_KEY, config.JWT_ALGORITHM)
        except jwt.JWTError as e:
            print(e)
            return None
        return encoded_jwt

    @classmethod
    async def refresh(cls, refresh_data: RefreshSchema):
        token_error = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token"
        )

        if refresh_data.refresh_token is None:
            raise token_error

        token_data = cls.decode_refresh_token(refresh_data.refresh_token)

        if token_data is None:
            raise token_error

        if token_data.get("sub") is None:
            raise token_error

        return await cls.create_tokens(
            user_id=token_data.get("sub"), only_access=True, is_registered=True, user_hash=token_data.get("hash")
        )

    @staticmethod
    async def create_tokens(
        user_id: int, user_hash: str, is_registered: bool, only_access: bool = False, security_mode: bool = False
    ) -> TokenSchema:
        authorize = JwtHandler()
        access_token = authorize.create_access_token(
            str(user_id), exp_time=config.ACCESS_TOKEN_EXPIRE_MINUTES, security_mode=security_mode, user_hash=user_hash
        )

        data = {
            "access_token": access_token,
            "access_time": config.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            "refresh_time": config.REFRESH_TOKEN_EXPIRE_MINUTES * 60,
        }

        if not only_access:
            refresh_token = authorize.create_refresh_token(
                str(user_id),
                user_hash=user_hash,
                exp_time=config.REFRESH_TOKEN_EXPIRE_MINUTES,
                security_mode=security_mode,
            )
            data.update({"refresh_token": refresh_token})
        return TokenSchema(**data, is_registered=is_registered)


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)

        if credentials:
            token = JwtHandler().decode_access_token(credentials.credentials)
            if token is None:
                return
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid auth token"
            )


jwt_h = JwtHandler()
