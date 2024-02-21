from fastapi import APIRouter

story_router=APIRouter()

@story_router.post("/add_story",status_code=201)
def add_story_api():
    pass

@story_router.get("/view_stories",status_code=200)
def  view_stories_api():
    pass

