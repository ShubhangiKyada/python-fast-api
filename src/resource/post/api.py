from fastapi import APIRouter

post_router=APIRouter()

@post_router.post("/create_post",status_code=201)
def create_post_api():
    pass

@post_router.get("/veiw_post",status_code=200)
def view_posts_api():
    pass

@post_router.put("/update_post",status_code=200)
def update_post_api():
    pass

@post_router.delete("/delete_post",status_code=204)
def  delete_post_api():
    pass