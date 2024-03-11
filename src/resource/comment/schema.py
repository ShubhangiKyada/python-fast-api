from pydantic import BaseModel
class CommentRequest(BaseModel):
    
    post_id:str
    comment :str
   
   