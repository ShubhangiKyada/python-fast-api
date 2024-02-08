from database.database import Sessionlocal
from src.resource.user.model import User

db = Sessionlocal()

def create_user(user_details):
    user_info = User(
        first_name=user_details.get("first_name"),
        last_name=user_details.get("last_name"),
        name=user_details.get("name"),
        email=user_details.get("email"),
        phone_no=user_details.get("phone_no"),
        password=user_details.get("password"),
    )
    db.add(user_info)
    db.commit()
    db.close()

    return "successfully created"

def log_in_user(user_details):
    email = user_details.get("email")
    phone_no = user_details.get("phone_no")
    password = user_details.get("password")

    user_data = None

    if email:
        user_data = db.query(User).filter_by(email=email, password=password).first()

    if phone_no and user_data is None:
        user_data = db.query(User).filter_by(phone_no=phone_no, password=password).first()

    if user_data:
        return "login successfully"

    return "user not found"

def change_password(user_details ):
    name = user_details.get("name")
    password = user_details.get("password")
    new_password=user_details.get("new_password")

    user_data = None

    if name:
        user_data = db.query(User).filter_by(name=name, password=password).first()

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
