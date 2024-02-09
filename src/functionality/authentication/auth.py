from database.database import Sessionlocal
from src.resource.user.model import User
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy.sql import or_
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

    return "successfully created"


def login_user(user_details):
    email = user_details.get('email')
    phone_no = user_details.get('phone_no')
    password = user_details.get('password')

    if email or phone_no:
        user_data = db.query(User).filter(or_(email==email,phone_no==phone_no)).first()
        check_password_hash(user_data.password,password)
    
    
    if user_data:
        return "user login successfully"
    
    return "user_not found"



# def log_in_user(user_details):
#     email = user_details.get("email")
#     phone_no = user_details.get("phone_no")
#     password = user_details.get("password")


#     if email:
#         user_data = db.query(User).filter_by(email=email).first()
#         check_password_hash(user_data.password,password)

#     if phone_no:
#         user_data = db.query(User).filter_by(phone_no=phone_no).first()
#         check_password_hash(user_data.password,password)

#     if user_data:
#         return "login successfully"

#     return "user not found"

def change_password(user_details ):
    name = user_details.get("name")
    password = user_details.get("password")
    new_password=generate_password_hash(user_details.get("new_password"))

  

    if name:
        user_data = db.query(User).filter_by(name=name).first()
        check_password_hash(user_data.password,password)
        
    if user_data:
        user_data.password = new_password
        db.commit()
        return "password successfully changed"

    return "user not found"

def get_user_info(user_details):
        id=user_details.get("id")
    
        user_data=db.query(User).filter_by(id=id).first()
        if user_data:    
            return user_data
        return "user not found"
