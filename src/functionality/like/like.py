from database.database import Sessionlocal
from src.resource.like.model import Like
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import uuid

db = Sessionlocal()



def like(post_id):
    id=uuid.uuid4()
    like_info = db.query(Like).filter_by(post_id=post_id).first()
    if like_info:
        existing_likes = like_info.count
        if existing_likes:
            like_info.count=existing_likes+1
        else:
            like_info.count = 1
        db.commit()
        db.close()
        return JSONResponse({"Message": "Post is liked"})
    else:
        like_info=Like(id=id, post_id=post_id, count=1)
        db.add(like_info)
        db.commit()
        db.close()
        raise HTTPException(status_code=404, detail="Post is Like by You")

def unlike(post_id):
    like_info = db.query(Like).filter_by(post_id=post_id).first()

    if like_info:
        existing_likes = like_info.count
        if existing_likes:
            like_info.count=existing_likes-1
        else:
            raise HTTPException(status_code=403,detail=" Like the Post First")
        db.commit()
        db.close()
        return JSONResponse({"Message": "Post is Unliked"})
    else:
        raise HTTPException(status_code=404, detail="Post not found")
