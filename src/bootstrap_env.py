import os
from dotenv import load_dotenv



load_dotenv("./config/shared.env")
load_dotenv("./config/local.env")

required_env_variables = [
    "DATABASE_URL_PARTIAL",
    "JWT_SECRET",
]

def load_env():
    for env_variable in required_env_variables:
        if not os.environ.get(env_variable):
            raise ValueError(f"Environment variable {env_variable} is not set")