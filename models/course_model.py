from sqlalchemy import Column, Integer, String

from core.configs import settings


class CourseModel(settings.DBBaseModel):
    __tablename__ = 'courses'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title: str = Column(String(100))
    classes: int = Column(Integer)
    hours: int = Column(Integer)
