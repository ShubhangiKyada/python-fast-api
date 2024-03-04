from database.database import Sessionlocal
from src.resource.post.model import Post
from fastapi.responses import JSONResponse


db = Sessionlocal()

def create_post(post_details,user_data):
    
    post_info = Post(
        photo = post_details.get("Photo"),
        description = post_details.get("Description"),
        location = post_details.get("Location"),
        user_id=user_data,
    )
    db.add(post_info)
    db.commit()
    db.close()

    return JSONResponse({"Message":"Post created"},status_code=201)


