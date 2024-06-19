from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.deps import get_db
from models.course_model import CourseModel
from schemas.course_schema import CourseSchema, CourseCreateSchema, CourseUpdateSchema

router = APIRouter()


@router.post("/", response_model=CourseSchema, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreateSchema, db: AsyncSession = Depends(get_db)):
    new_course = CourseModel(**course.dict())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course


@router.get("/", response_model=List[CourseSchema])
async def get_courses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CourseModel))
    courses = result.scalars().all()
    return courses


@router.get("/{course_id}", response_model=CourseSchema)
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CourseModel).where(CourseModel.id == course_id))
    course = result.scalar_one_or_none()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.put("/{course_id}", response_model=CourseSchema)
async def update_course(course_id: int, course: CourseUpdateSchema, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CourseModel).where(CourseModel.id == course_id))
    existing_course = result.scalar_one_or_none()
    if existing_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in course.dict(exclude_unset=True).items():
        setattr(existing_course, key, value)
    await db.commit()
    await db.refresh(existing_course)
    return existing_course


@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CourseModel).where(CourseModel.id == course_id))
    existing_course = result.scalar_one_or_none()
    if existing_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    await db.delete(existing_course)
    await db.commit()
    return None
