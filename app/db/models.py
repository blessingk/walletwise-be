from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.db.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)  # You can create a User table later
    bank_name = Column(String, index=True)
    account_number = Column(String)
    date = Column(Date)
    description = Column(String)
    amount = Column(Float)
    category = Column(String)
