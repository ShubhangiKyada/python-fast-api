from fastapi import APIRouter
from src.functionality.like.like import like,unlike

like_router=APIRouter()

@like_router.post("/like/{post_id}",status_code=201)
def like_api(post_id):
    like_info=like(post_id)
    return like_info

@like_router.delete("/like/{post_id}",status_code=204)
def  unlike_api(post_id):
    like_info=unlike(post_id)
    return like_info
   
