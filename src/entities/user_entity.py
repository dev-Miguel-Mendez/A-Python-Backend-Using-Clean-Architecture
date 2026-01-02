import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from interfaces.db.declarative_base import Base
from interfaces.schemas.users.create_user_schemas import UserOut






class User(Base):

    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        primary_key=True, 
        init=False, 
        default=lambda: str(uuid.uuid4())
    )
    user_name: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    def to_dict(self) -> UserOut:
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email
        }