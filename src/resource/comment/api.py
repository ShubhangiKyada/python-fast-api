from fastapi import APIRouter

comment_router=APIRouter()

@comment_router.post("/comment",status_code=201)
def  add_comment_api():
    pass

@comment_router.get( "/comments", status_code = 200 )
def show_comments_api ():
    pass

@comment_router.delete( "/comment", status_code = 204 )
def delete_comment_api():
    pass