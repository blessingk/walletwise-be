from pydantic import BaseModel

class QuizBase(BaseModel):
    title: str

class Quiz(QuizBase):
    id: int
    course_id: int

    class Config:
        orm_mode = True
