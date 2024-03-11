from pydantic import BaseModel
from typing import Optional

class PostRequest(BaseModel):
    
    photo : str
    description : Optional[str] = None
    location : Optional[str] = None
   