from pydantic import BaseModel

class QuestionBase(BaseModel):
    text: str

class Question(QuestionBase):
    id: int
    quiz_id: int

    class Config:
        orm_mode = True
