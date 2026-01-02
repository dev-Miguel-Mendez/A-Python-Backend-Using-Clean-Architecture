from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from entities.user_entity import User 
from interfaces.http.dependencies.db_session_dependency import get_db_session
from interfaces.http.dependencies.jwt_dependency import get_jwt_provider_singleton
from interfaces.http.exceptions.custom_exception_instances import Unauthorized
from interfaces.jwt.jwt_provider import JWTPayload, JWTProvider
from interfaces.db.repositories.user_repository import UserRepository


async def get_auth_user_dependency (
    request: Request, 
    jwt_provider: JWTProvider = Depends(get_jwt_provider_singleton),
    session: AsyncSession = Depends(get_db_session)
) -> User:
    payload: JWTPayload = jwt_provider.verify_jwt(request.cookies.get('AUTH_TOKEN') or '')
    user_repo = UserRepository(session)
    user = await user_repo.find_user_by_id(payload['user_id'])

    if not user: raise Unauthorized('User not found for provided token')

    return user
    
    