from pydantic import BaseModel
from typing import Optional
import uuid

class UserRequest(BaseModel):
    
    first_name : Optional[str]
    last_name : Optional[str]
    name : Optional[str]
    email : Optional[str]
    phone_no : str
    password :str


class UserLoginSchema(BaseModel):
    email : Optional[str] = None
    phone_no : Optional[str] = None
    password : str

class UserChangePasswordSchema(BaseModel):
    name:str
    password:str
    new_password:str

class UserInformation(BaseModel):
    id:str=None
