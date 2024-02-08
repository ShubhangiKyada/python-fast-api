from fastapi import APIRouter
from src.resource.authentication.schema import UserRequest,UserLoginSchema,UserChangePasswordSchema,UserInformation
from src.functionality.authentication.auth import create_user,log_in_user,change_password,get_user_info
from src.resource.authentication.serializer import serializer_use 
auth_router= APIRouter()

@auth_router.post("/signup",status_code=201)
def create_user_api(user_data:UserRequest):
    user_info=create_user(user_data.model_dump())
    return user_info

@auth_router.post("/login",status_code=200)
def log_in_api(user_data:UserLoginSchema):
    user_info=log_in_user(user_data.model_dump())
    return user_info

@auth_router.post("/change_password",status_code=200)
def change_password_api(user_data:UserChangePasswordSchema):
    user_info=change_password(user_data.model_dump())
    return user_info

@auth_router.get("/user_info",status_code=200)
def get_user_info_api(user_data:UserInformation):
    user_info=get_user_info(user_data.model_dump())
    output =serializer_use(user_info)
    return output 