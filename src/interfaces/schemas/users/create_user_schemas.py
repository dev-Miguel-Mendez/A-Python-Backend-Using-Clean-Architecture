from typing import TypedDict
from pydantic  import  EmailStr, TypeAdapter

from interfaces.schemas.shared import StandardResponse


#! I didn't use the Pydantic BaseModel this because .model_dump() gives  the type "[str, Any]"

#$ FastAPI can validate the body using this TypedDict.
class UserCreateDict(TypedDict):
    user_name: str
    password: str
    email: EmailStr



create_user_validator = TypeAdapter(UserCreateDict) #$ This can act as a services validator.
#$ Since FastAPI already validates the body with the TypedDict, this is extra in case, for example, have Redis/RabbitMQ and want to validate it into that same TypedDict.



class UserOut(TypedDict):
    id: str
    user_name: str
    email: str


class CreateUserResponse(StandardResponse):
    data: UserOut