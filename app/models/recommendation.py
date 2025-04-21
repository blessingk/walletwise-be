from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.db.database import Base

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    category = Column(String)
