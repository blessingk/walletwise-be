from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    partner_id = Column(Integer, ForeignKey("partners.id"))
    status = Column(String(50), default="pending")  # 'pending', 'sent', 'failed', 'accepted'
    response = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    partner = relationship("Partner")
