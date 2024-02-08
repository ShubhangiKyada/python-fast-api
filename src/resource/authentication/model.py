
from database.database import Base
from sqlalchemy import Column,VARCHAR,Boolean,DateTime,ForeignKey
from uuid import uuid4
from datetime import datetime
from src.resource.user.model import User

class Otp(Base):
    __tablename__ = "OTP"
    id = Column(VARCHAR(51), primary_key=True,default=uuid4())
    user_id =Column(VARCHAR(51),ForeignKey(User.id,ondelete="CASCADE"))
    otp = Column(VARCHAR(51))
    created_at = Column(DateTime, default=datetime.utcnow())
    expiry_at = Column(DateTime)
    is_used = Column(Boolean, default=False)
    use_for = Column(VARCHAR(256),nullable=False)