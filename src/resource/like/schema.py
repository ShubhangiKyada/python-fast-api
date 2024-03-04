from pydantic import BaseModel
from typing import Optional

class LikeRequest(BaseModel):
    
    post_id : str
   
   