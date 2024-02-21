from fastapi import APIRouter

like_router=APIRouter()

@like_router.post("/like_post",status_code=201)
def like_post_api():
    pass

@like_router.delete("/unlike_post",status_code=204)
def  unlike_post_api():
    pass
