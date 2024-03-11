from pydantic import BaseModel


class StroyRequest(BaseModel):
    
    photo : str
    
   