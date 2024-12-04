from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import DepartmentNotFound, DepartmentAlreadyExists
from project.infrastructure.postgres.models import Department
from project.schemas.departments import DepartmentsSchema, DepartmentsCreateUpdateSchema


class DepartmentsRepository:
    _collection = Department

    async def get_all_departments(self, session: AsyncSession) -> list[DepartmentsSchema]:
        query = select(self._collection)
        departments = await session.scalars(query)
        return [DepartmentsSchema.model_validate(obj=department) for department in departments.all()]

    async def get_department_by_id(self, session: AsyncSession, department_id: int) -> DepartmentsSchema:
        query = select(self._collection).where(self._collection.department_id == department_id)
        department = await session.scalar(query)
        if not department:
            raise DepartmentNotFound(_id=department_id)
        return DepartmentsSchema.model_validate(obj=department)

    async def create_department(self, session: AsyncSession, department: DepartmentsCreateUpdateSchema) -> DepartmentsSchema:
        query = insert(self._collection).values(department.model_dump()).returning(self._collection)
        try:
            created_department = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise DepartmentAlreadyExists(name=department.name)
        return DepartmentsSchema.model_validate(obj=created_department)

    async def update_department(self, session: AsyncSession, department_id: int, department: DepartmentsCreateUpdateSchema) -> DepartmentsSchema:
        query = (
            update(self._collection)
            .where(self._collection.department_id == department_id)
            .values(department.model_dump())
            .returning(self._collection)
        )
        updated_department = await session.scalar(query)
        if not updated_department:
            raise DepartmentNotFound(_id=department_id)
        return DepartmentsSchema.model_validate(obj=updated_department)

    async def delete_department(self, session: AsyncSession, department_id: int) -> None:
        query = delete(self._collection).where(self._collection.department_id == department_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise DepartmentNotFound(_id=department_id)
