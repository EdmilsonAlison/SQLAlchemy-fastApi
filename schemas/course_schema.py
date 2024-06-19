from typing import Optional

from pydantic import BaseModel


class CourseCreateSchema(BaseModel):
    title: str
    classes: int
    hours: int

    class Config:
        orm_mode = True


class CourseUpdateSchema(BaseModel):
    title: Optional[str]
    classes: Optional[int]
    hours: Optional[int]

    class Config:
        orm_mode = True


class CourseSchema(CourseCreateSchema):
    id: Optional[int]
