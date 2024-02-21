from fastapi import APIRouter, Depends
from typing import Annotated
from src.utils.validator import authorization
from src.resource.authentication.schema import (
    UserLoginSchema,
    UserChangePasswordSchema,
)
from src.functionality.authentication.auth import (
    login_user,
    change_password,
)
from src.functionality.user.user import get_user_info,create_user

auth_router = APIRouter()

@auth_router.post("/login", status_code=200)
def login_api(user_data: UserLoginSchema):
    user_info = login_user(user_data.model_dump())
    return user_info


@auth_router.post("/change_password", status_code=200)
def change_password_api(
    user_data: UserChangePasswordSchema,
    user_information: Annotated[dict, Depends(authorization)],):
    user_info = change_password(user_data.model_dump(), user_information.get("id"))
    return user_info
