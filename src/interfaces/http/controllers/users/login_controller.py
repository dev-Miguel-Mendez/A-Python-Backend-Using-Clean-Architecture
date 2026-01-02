from fastapi import Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from interfaces.db.repositories.user_repository import UserRepository
from interfaces.hashing.async_hasher_bcrypt import AsyncHasherBcrypt
from interfaces.http.dependencies.db_session_dependency import get_db_session
from interfaces.http.dependencies.hash_dependency import get_hasher_singleton
from interfaces.http.dependencies.jwt_dependency import get_jwt_provider_singleton
from interfaces.jwt.jwt_provider import JWTProvider
from interfaces.schemas.shared import StandardResponse
from interfaces.schemas.users.login_user_schema import UserLoginDict
from use_cases.users.login_user_use_case import LoginUserUseCase

async def login_controller (
    body: UserLoginDict, 
    response: Response, 
    session: AsyncSession = Depends(get_db_session),
    hasher: AsyncHasherBcrypt = Depends(get_hasher_singleton),
    jwt: JWTProvider = Depends(get_jwt_provider_singleton)
) -> StandardResponse:

    repo = UserRepository(session)

    token: str = await LoginUserUseCase(repo, hasher, jwt).execute(user_data=body)

    response.set_cookie(key="AUTH_TOKEN", value=token, httponly=True,)

    return {
        "success": True,
        "message": "User logged in successfully",
    }