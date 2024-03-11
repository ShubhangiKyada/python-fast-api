from sqlalchemy import VARCHAR, Boolean, String, Column,DateTime,ForeignKey
from database.database import Base
from uuid import uuid4
from datetime import datetime
from src.resource.user.model import User

class Story(Base):
    __tablename__ = "Story"
    id = Column(String(256),primary_key=True,default= uuid4())
    photo=Column(String(256))
    user_id = Column(VARCHAR(256),ForeignKey(User.id,ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.utcnow())