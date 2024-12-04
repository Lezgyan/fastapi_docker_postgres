from sqlalchemy import insert, update, delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import CourseOfTreatmentNotFound, CourseOfTreatmentAlreadyExists
from project.infrastructure.postgres.models import CourseOfTreatment
from project.schemas.course_of_treatment import CourseOfTreatmentSchema, CourseOfTreatmentCreateUpdateSchema


class CourseOfTreatmentRepository:
    _collection = CourseOfTreatment

    async def get_all_courses(self, session: AsyncSession) -> list[CourseOfTreatmentSchema]:
        query = select(self._collection)
        courses = await session.scalars(query)
        return [CourseOfTreatmentSchema.model_validate(obj=course) for course in courses.all()]

    async def get_course_by_id(self, session: AsyncSession, course_id: int) -> CourseOfTreatmentSchema:
        query = select(self._collection).where(self._collection.id == course_id)
        course = await session.scalar(query)
        if not course:
            raise CourseOfTreatmentNotFound(_id=course_id)
        return CourseOfTreatmentSchema.model_validate(obj=course)

    async def create_course(self, session: AsyncSession, course: CourseOfTreatmentCreateUpdateSchema) -> CourseOfTreatmentSchema:
        query = insert(self._collection).values(course.model_dump()).returning(self._collection)
        try:
            created_course = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise CourseOfTreatmentAlreadyExists()
        return CourseOfTreatmentSchema.model_validate(obj=created_course)

    async def update_course(self, session: AsyncSession, course_id: int, course: CourseOfTreatmentCreateUpdateSchema) -> CourseOfTreatmentSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == course_id)
            .values(course.model_dump())
            .returning(self._collection)
        )
        updated_course = await session.scalar(query)
        if not updated_course:
            raise CourseOfTreatmentNotFound(_id=course_id)
        return CourseOfTreatmentSchema.model_validate(obj=updated_course)

    async def delete_course(self, session: AsyncSession, course_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == course_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise CourseOfTreatmentNotFound(_id=course_id)
