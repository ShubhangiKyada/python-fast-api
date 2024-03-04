from pydantic import BaseModel
from typing import Optional

class StroyRequest(BaseModel):
    
    photo : str
    description : Optional[str]
    location : Optional[str]
   