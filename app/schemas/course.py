from pydantic import BaseModel

class CourseBase(BaseModel):
    title: str
    description: str
    level: str

class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True
