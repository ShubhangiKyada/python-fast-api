from sqlalchemy import VARCHAR, Column,DateTime,ForeignKey
from database.database import Base
from uuid import uuid4
from datetime import datetime
from src.resource.user.model import User
from src.resource.post.model import Post

class Like(Base):
    __tablename__ = "Like"
    id = Column(VARCHAR(256),primary_key=True,default= uuid4())
    post_id = Column(VARCHAR(256),ForeignKey(User.id,ondelete="CASCADE"))
    count = Column(VARCHAR(256) ,nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
   