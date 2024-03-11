from fastapi import APIRouter,Depends
from typing import Annotated
from src.utils.validator import authorization
from src.resource.comment.schema import CommentRequest
from src.functionality.comment.comment import create_comment,view_comment,delete_comment

comment_router = APIRouter()

@comment_router.post("/comment",status_code=201)
def add_comment_api( comment_data:CommentRequest,user_data: Annotated[dict, Depends(authorization)]):
    comment_info = create_comment(comment_data.model_dump(), user_data.get("id"))
    return comment_info

@comment_router.get("/comment/{post_id}",status_code=200)
def view_comment_api(post_id):
    comment_info = view_comment(post_id)
    return comment_info

@comment_router.delete("/comment/{post_id}",status_code=204)
def delete_comment_api(post_id,user_data: Annotated[dict, Depends(authorization)]):
    comment_info = delete_comment(post_id,user_data.get("id"))
    return comment_info