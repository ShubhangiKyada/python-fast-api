from fastapi import APIRouter,Depends
from typing import Annotated
from src.utils.validator import authorization
from src.resource.story.schema import StroyRequest
from src.functionality.story.story import create_story,view_story

story_router=APIRouter()

@story_router.post("/story",status_code=201)
def add_story_api(story_data:StroyRequest, user_data:Annotated[dict, Depends(authorization)]):
    post_info = create_story(story_data.model_dump(),user_data.get("id"))
    return post_info
    

@story_router.get("/stories/{user_id}",status_code=200)
def  view_stories_api(user_id):
    story_info=view_story(user_id)
    return story_info
    

