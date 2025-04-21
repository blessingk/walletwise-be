from pydantic import BaseModel
from datetime import datetime

class PartnerBase(BaseModel):
    name: str
    email: str
    webhook_url: str
    phone: str

class PartnerCreate(PartnerBase):
    pass

class Partner(PartnerBase):
    id: int
    active: bool
    created_at: datetime

    class Config:
        orm_mode = True
