







from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from interfaces.http.exceptions.custom_exception_instances  import AppError
from interfaces.http.exceptions.exception_handlers import app_error_handler, global_exception_handler, validation_error_handler
from interfaces.http.routers.users_router import users_router







app = FastAPI()

app.include_router(users_router)


app.exception_handler(RequestValidationError)(validation_error_handler)
app.exception_handler(Exception)(global_exception_handler)
app.exception_handler(AppError)(app_error_handler)