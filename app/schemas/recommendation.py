from pydantic import BaseModel
from datetime import datetime

class RecommendationBase(BaseModel):
    title: str
    description: str
    category: str
    severity: int = 1

class RecommendationCreate(RecommendationBase):
    pass

class Recommendation(RecommendationBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
