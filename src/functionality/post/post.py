from database.database import Sessionlocal
from src.resource.post.model import Post
from src.resource.comment.model import Comment
from src.resource.like.model import Like
from src.resource.post.serializer import serializer_for_getpost
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import uuid


db = Sessionlocal()

def create_post(post_details,user_data):
    id=uuid.uuid4()
    post_info = Post(
        id=id,
        photo = post_details.get("photo"),
        description = post_details.get("description"),
        location = post_details.get("location"),
        user_id=user_data,
    )
    db.add(post_info)
    db.commit()
    db.close()

    return JSONResponse({"Message":"Post created","Post_Id":str(id)},status_code=201)

def get_post(user_id):
    post_data = (
        db.query(Post)
        .filter_by(user_id=user_id, is_active=True, is_deleted=False)
        .first()
    )
    post_list=[]
    
    if post_data :
        for post in post_data:
            comment_data = db.query(Comment).filter_by(post_id=post.id).all() 

            like_data = db.query(Like).filter_by(post_id=post.id).all() 

            filter_data = serializer_for_getpost(post, comment_data, like_data)
            
            post_list.append(filter_data)
        return JSONResponse({"Post": post_list})
    else:
            raise HTTPException(status_code=404, detail="Post not found")


def update_post(post_id,post_details , user_id):

    post_data = (
        db.query(Post).filter_by(id=post_id, is_active=True, is_deleted=False).first()
    )
    if post_data:
        if post_data.user_id == user_id:
            post_data.photo = post_details.get("photo")
            if "description" in post_details:
                post_data.description = post_details.get("description")
            if "location" in post_details:
                post_data.location = post_details.get("location")
            db.commit()
            db.close()
            return JSONResponse({"Message": "post upadate successfully"})
        else:
            raise HTTPException(
                status_code=401, detail="you have no rights to upadate this"
            )
    else:
        raise HTTPException(status_code=404, detail="Post not found")


def delete_post(post_id, user_id):
    post_data = (
        db.query(Post).filter_by(id=post_id, is_active=True, is_deleted=False).first()
    )
    if post_data:
        if post_data.user_id == user_id:
            post_data.is_active = False
            post_data.is_deleted = True
            db.commit()
            return  JSONResponse({"Message": "Post deleted Successfully"})


