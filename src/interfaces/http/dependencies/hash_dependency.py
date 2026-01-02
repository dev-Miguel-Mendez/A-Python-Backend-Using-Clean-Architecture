
from interfaces.hashing.async_hasher_bcrypt import AsyncHasherBcrypt


async_hasher_bcrypt_singleton = AsyncHasherBcrypt()

def get_hasher_singleton():
    return async_hasher_bcrypt_singleton