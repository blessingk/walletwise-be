from pydantic import BaseModel
from datetime import date

class TransactionCreate(BaseModel):
    user_id: int
    bank_name: str
    account_number: str
    date: date
    description: str
    amount: float
    category: str

class Transaction(TransactionCreate):
    id: int

    class Config:
        orm_mode = True
