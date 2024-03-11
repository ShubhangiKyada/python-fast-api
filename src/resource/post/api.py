from fastapi import APIRouter,Depends
from typing import Annotated
from src.utils.validator import authorization
from src.resource.post.schema import PostRequest
from src.functionality.post.post import create_post,get_post,update_post,delete_post

post_router=APIRouter()

@post_router.post("/post",status_code=201)
def create_post_api(post_data:PostRequest, user_data:Annotated[dict, Depends(authorization)]):
    post_info = create_post(post_data.model_dump(),user_data.get("id"))
    return post_info

@post_router.get("/post/{user_id}",status_code=200)
def view_posts_api(user_id):
    post_info = get_post(user_id)
    return post_info

@post_router.patch("/post/{post_id}",status_code=200)
def update_post_api(post_id,post_data:PostRequest, user_data:Annotated[dict, Depends(authorization)]):
    post_info = update_post(post_id,post_data.model_dump(),user_data.get("id"))
    return post_info

@post_router.delete("/post/{post_data}",status_code=204)
def  delete_post_api(post_data, user_data:Annotated[dict, Depends(authorization)]):
    post_info = delete_post(post_data,user_data.get("id"))
    return post_info
