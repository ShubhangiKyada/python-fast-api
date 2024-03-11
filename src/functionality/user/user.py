from database.database import Sessionlocal
from src.resource.user.model import User
from werkzeug.security import generate_password_hash
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.resource.authentication.serializer import getuser_serializer

db = Sessionlocal()

def create_user(user_details):

    user_info = User(
        first_name=user_details.get("first_name"),
        last_name=user_details.get("last_name"),
        name=user_details.get("name"),
        email=user_details.get("email"),
        phone_no=user_details.get("phone_no"),
        password=generate_password_hash(user_details.get("password")),
    )
    db.add(user_info)
    db.commit()
    db.close()

    return JSONResponse({"message": "successfully created"})


def get_user_info(user_id):

    user_data = (
        db.query(User).filter_by(id=user_id, is_active=True, is_deleted=False).first()
    )

    if user_data:
        filter_data=getuser_serializer(user_data)
        db.commit()
        db.close()
        return JSONResponse({"Data": filter_data})
    else:
        raise HTTPException(status_code=404, detail="User Not Found")
    
def  delete_user(user_id,user_details):
    if user_id==user_details.get("id"):

        user_data = (
            db.query(User).filter_by(id=user_id, is_active=True, is_deleted=False).first()
        )
        if user_data:
            user_data.is_active=False
            user_data.is_deleted=True
            db.commit()
            db.close()
            return JSONResponse({"message":"User deletd Successfully"})
    else:
        raise HTTPException(status_code=409,detail="Invalid User id")