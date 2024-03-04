from fastapi import APIRouter,Depends
from typing import Annotated
from src.utils.validator import authorization
from src.resource.post.schema import PostRequest
from src.functionality.post.post import create_post

post_router=APIRouter()

@post_router.post("/create_post",status_code=201)
def create_post_api(post_data:PostRequest, user_data:Annotated[dict, Depends(authorization)]):
    post_info = create_post(post_data.model_dump(),user_data.get("id"))
    return post_info

@post_router.get("/post",status_code=200)
def view_posts_api():
    pass

@post_router.put("/post",status_code=200)
def update_post_api():
    pass

@post_router.delete("/delete_post",status_code=204)
def  delete_post_api():
    pass