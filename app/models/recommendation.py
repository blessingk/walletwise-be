from sqlalchemy import Column, Integer, String, Text, DateTime
from app.db.database import Base
from datetime import datetime

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(100))
    severity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
