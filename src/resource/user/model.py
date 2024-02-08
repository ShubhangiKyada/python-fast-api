from sqlalchemy import VARCHAR, Boolean,Integer, String, Column,DateTime
from database.database import Base
from uuid import uuid4
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(String(256),primary_key=True,default= uuid4())
    first_name=Column(VARCHAR(30))
    last_name=Column(VARCHAR(30))
    name = Column(VARCHAR(30))
    email = Column(String(256), nullable=False)
    password = Column(VARCHAR(255), nullable=False)
    phone_no = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    is_verify = Column(Boolean, default=False)
