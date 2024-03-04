from sqlalchemy import VARCHAR, Boolean, Column,DateTime,ForeignKey,JSON
from database.database import Base
from uuid import uuid4
from datetime import datetime
from src.resource.user.model import User
from src.resource.post.model import Post

class Comment(Base):
    __tablename__ = "Comments"
    id = Column(VARCHAR(36), primary_key=True, default=uuid4())
    post_id = Column(VARCHAR(256),ForeignKey(User.id,ondelete="CASCADE"))
    comment= Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow())
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
   
   