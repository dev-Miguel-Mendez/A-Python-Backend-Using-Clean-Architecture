from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from entities.user_entity import User
from interfaces.schemas.users.create_user_schemas import UserCreateDict


class UserRepository():
    def __init__(self, session: AsyncSession):
        self.session = session
    

    async def find_user_by_email(self, email:str):
        existing_email_user_result = await self.session.execute(
            select(User).where(User.email == email)
        )

        existing: User | None = existing_email_user_result.scalars().first()
        return existing

    async def find_user_by_id(self, id: str):
        existing_email_user_result = await self.session.execute(
            select(User).where(User.id == id)
        )

        existing: User | None = existing_email_user_result.scalars().first()
        return existing

    async def create_user(self, user_data: UserCreateDict):
        
        
        user = User(**user_data)

        self.session.add(user)

        await self.session.commit()

        return user