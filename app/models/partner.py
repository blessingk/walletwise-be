from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db.database import Base
from datetime import datetime

class Partner(Base):
    __tablename__ = "partners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255))
    webhook_url = Column(String(500))  # Endpoint to receive leads
    phone = Column(String(20))
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
