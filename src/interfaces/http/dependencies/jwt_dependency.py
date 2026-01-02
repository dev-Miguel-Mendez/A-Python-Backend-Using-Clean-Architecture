
from interfaces.jwt.jwt_provider import JWTProvider


jwt_manager_singleton = JWTProvider()

def get_jwt_provider_singleton():
    return jwt_manager_singleton