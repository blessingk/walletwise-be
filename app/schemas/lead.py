from pydantic import BaseModel
from datetime import datetime

class LeadBase(BaseModel):
    user_id: int
    partner_id: int
    status: str = "pending"
    response: str = None

class LeadCreate(LeadBase):
    pass

class Lead(LeadBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
