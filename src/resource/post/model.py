from sqlalchemy import VARCHAR, Boolean, Column,DateTime,ForeignKey
from database.database import Base
from uuid import uuid4
from datetime import datetime
from src.resource.user.model import User

class Post(Base):
    __tablename__ = "Post"
    id = Column(VARCHAR(256),primary_key=True,default= uuid4())
    user_id = Column(VARCHAR(256),ForeignKey(User.id,ondelete="CASCADE"))
    description=Column(VARCHAR(30))
    location=Column(VARCHAR(30), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    
