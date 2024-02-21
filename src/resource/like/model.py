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
    user_id = Column(VARCHAR(256),ForeignKey(Post.id,ondelete="CASCADE"))
    description=Column(VARCHAR(30))
    location=Column(VARCHAR(30), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
   