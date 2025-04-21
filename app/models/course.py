from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    level = Column(String)
