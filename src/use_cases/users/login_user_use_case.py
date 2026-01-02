from interfaces.db.repositories.user_repository import UserRepository
from interfaces.hashing.async_hasher_bcrypt import AsyncHasherBcrypt
from interfaces.http.exceptions.custom_exception_instances import Unauthorized
from interfaces.jwt.jwt_provider import JWTProvider
from interfaces.schemas.users.login_user_schema import UserLoginDict


class LoginUserUseCase():

    def __init__(
        self,
        user_repository: UserRepository, 
        hasher: AsyncHasherBcrypt, 
        jwt: JWTProvider
    ):
        self.jwt_provider = jwt
        self.user_repository = user_repository
        self.hasher = hasher



    async def execute(self, *, user_data: UserLoginDict):
        existing_user_with_email = await self.user_repository.find_user_by_email(user_data['email'])

        if not existing_user_with_email: raise Unauthorized(message='Invalid email or password')

        password_match = await self.hasher.verify_password_async(
            unhashed_password=user_data["password"],
            hashed_password=existing_user_with_email.password
        )

        if not password_match: raise Unauthorized(message='Invalid email or password')
        
        return self.jwt_provider.generate_jwt(user_id=existing_user_with_email.id)
        