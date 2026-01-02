from entities.user_entity import User 
from interfaces.db.repositories.user_repository import UserRepository
from interfaces.hashing.async_hasher_bcrypt import AsyncHasherBcrypt
from interfaces.http.dependencies.db_session_dependency import get_db_session
from interfaces.http.dependencies.hash_dependency import get_hasher_singleton
from interfaces.schemas.users.create_user_schemas import CreateUserResponse, UserCreateDict
from  use_cases.users.create_user_use_case import CreateUserUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends






async def create_user_controller (
    body: UserCreateDict, 
    session: AsyncSession = Depends(get_db_session),
    hasher: AsyncHasherBcrypt = Depends(get_hasher_singleton)
) -> CreateUserResponse: 
# async def create_user_controller (body: UserCreateDict = Body()): #$ Using "Body()" is not strictly necessary UNLESS:
    #$ 1.  YOU WANT TO MAKE IT OPTIONAL (use `Body(None)` ).
    #$ 2. For some reason FastAPI can't infer that UserCreateDict is the body.

    repo = UserRepository(session)

    new_user: User = await CreateUserUseCase(repo, hasher).execute(user_data=body)

    return {
        "success": True,
        "message": "User created successfully",
        "data": new_user.to_dict(),
    }