from sqlalchemy import delete, update, insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import QualificationTypeNotFound, QualificationTypeAlreadyExists
from project.infrastructure.postgres.models import QualificationType
from project.schemas.qualification_type import QualificationTypeSchema, QualificationTypeCreateUpdateSchema


class QualificationTypeRepository:
    _collection = QualificationType

    async def get_all_qualification_types(self, session: AsyncSession) -> list[QualificationTypeSchema]:
        query = select(self._collection)
        qualification_types = await session.scalars(query)
        return [QualificationTypeSchema.model_validate(obj=qt) for qt in qualification_types.all()]

    async def get_qualification_type_by_id(self, session: AsyncSession, qt_id: int) -> QualificationTypeSchema:
        query = select(self._collection).where(self._collection.id == qt_id)
        qualification_type = await session.scalar(query)
        if not qualification_type:
            raise QualificationTypeNotFound(_id=qt_id)
        return QualificationTypeSchema.model_validate(obj=qualification_type)

    async def create_qualification_type(self, session: AsyncSession, qt: QualificationTypeCreateUpdateSchema) -> QualificationTypeSchema:
        query = insert(self._collection).values(qt.model_dump()).returning(self._collection)
        try:
            created_qualification_type = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise QualificationTypeAlreadyExists(name=qt.name)
        return QualificationTypeSchema.model_validate(obj=created_qualification_type)

    async def update_qualification_type(self, session: AsyncSession, qt_id: int, qt: QualificationTypeCreateUpdateSchema) -> QualificationTypeSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == qt_id)
            .values(qt.model_dump())
            .returning(self._collection)
        )
        updated_qualification_type = await session.scalar(query)
        if not updated_qualification_type:
            raise QualificationTypeNotFound(_id=qt_id)
        return QualificationTypeSchema.model_validate(obj=updated_qualification_type)

    async def delete_qualification_type(self, session: AsyncSession, qt_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == qt_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise QualificationTypeNotFound(_id=qt_id)
