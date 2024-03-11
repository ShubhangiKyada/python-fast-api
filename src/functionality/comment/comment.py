from database.database import Sessionlocal
from src.resource.comment.model import Comment
from src.resource.comment.serializer import view_commnet_serializer
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import uuid

db = Sessionlocal()

id=uuid.uuid4()

def create_comment(comment_details, user_id):
    
    
    comment_={user_id:comment_details.get('comment')} 

    comment_info = (db.query(Comment).filter_by(post_id = comment_details.get('post_id')).first())
    
    if comment_info:
        existing_comment = comment_info.comment.copy()
        if existing_comment:
            if user_id not in existing_comment:
                existing_comment.update(comment_)
                comment_info.comment=existing_comment
                db.commit()
                return JSONResponse({"Message": "Comment created successfully"})
            else:
                comment_info.comment[user_id]= comment_details.get("comment")  
            db.add(comment_info)
        db.commit()
        db.close()
        return JSONResponse({"Message": "Comment updated successfully"})
    else:
        comment_info=Comment(id=id , post_id=comment_details.get('post_id'),comment=comment_)
        db.add(comment_info)
        db.commit()
        db.close()
        return {"Message":"Comment added to the Post"}
    
def view_comment(post_id):
    comment_info = db.query(Comment).filter_by(post_id = post_id).all()
    if  comment_info:
        filter_data=view_commnet_serializer(comment_info)
        return JSONResponse({"Data":filter_data})
    else:
        raise HTTPException(status_code=404,detail="Comment not found")
    

def delete_comment(post_id, user_id):
    comment_info_data= (db.query(Comment).filter_by(post_id = post_id).first())
    
    if comment_info_data:
        comment_data=comment_info_data.comment.copy()
        if user_id in comment_data:
            del comment_data[user_id]
            comment_info_data.comment=comment_data
            db.commit()
            return JSONResponse({"Message": "Comment deleted successfully"})
        else:
            raise HTTPException(status_code=404, detail="Comment not found for this user")
    else:
        raise HTTPException(status_code=404, detail="Comment not found")