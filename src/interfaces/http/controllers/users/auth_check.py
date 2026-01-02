from fastapi import Depends

from entities.user_entity import User 
from interfaces.http.dependencies.auth_dependency import get_auth_user_dependency
from interfaces.schemas.shared import StandardResponse


async def auth_check_controller (authenticated_user: User = Depends(get_auth_user_dependency)) -> StandardResponse:
    return {
        "success": True,
        "message": "User is authenticated",
        "data": authenticated_user.to_dict()
    }