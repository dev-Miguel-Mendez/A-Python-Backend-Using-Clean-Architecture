from interfaces.db.repositories.user_repository import UserRepository
from interfaces.hashing.async_hasher_bcrypt import AsyncHasherBcrypt
from interfaces.http.exceptions.custom_exception_instances  import BadRequest
from interfaces.schemas.users.create_user_schemas import UserCreateDict




class CreateUserUseCase():

    def __init__(
        self, 
        user_repository: UserRepository, #! Pass the repo and don't let the use case know about the session.
        hasher: AsyncHasherBcrypt
    ): 
        self.user_repository = user_repository
        self.hasher = hasher

    async def execute(self, *, user_data: UserCreateDict):

        existing_user_with_email = await self.user_repository.find_user_by_email(user_data['email'])

        if existing_user_with_email: raise BadRequest(message="User with this email already exists")

        hashed_password = await self.hasher.hash_password_async(user_data['password'])

        user_data['password'] = hashed_password

        return await self.user_repository.create_user(user_data)