from pydantic import BaseModel
from datetime import datetime

class UserRecommendationBase(BaseModel):
    user_id: int
    recommendation_id: int
    is_dismissed: bool = False
    is_completed: bool = False

class UserRecommendationCreate(UserRecommendationBase):
    pass

class UserRecommendation(UserRecommendationBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
