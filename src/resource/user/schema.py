from pydantic import BaseModel
from typing import Optional


class UserRequest(BaseModel):
    
    first_name : Optional[str]
    last_name : Optional[str]
    name : Optional[str]
    email : Optional[str]
    phone_no : int
    password :str