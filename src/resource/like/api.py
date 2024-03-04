from fastapi import APIRouter

like_router=APIRouter()

@like_router.post("/post",status_code=201)
def like_api():
    pass

@like_router.delete("/post",status_code=204)
def  unlike_api():
    pass
