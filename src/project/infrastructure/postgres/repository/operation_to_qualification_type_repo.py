from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import OperationToQualificationTypeNotFound, OperationToQualificationTypeAlreadyExists
from project.infrastructure.postgres.models import OperationToQualificationType
from project.schemas.operation_to_qualification_type import OperationToQualificationTypeSchema, \
    OperationToQualificationTypeCreateUpdateSchema


class OperationToQualificationTypeRepository:
    _collection = OperationToQualificationType

    async def get_all_links(self, session: AsyncSession) -> list[OperationToQualificationTypeSchema]:
        query = select(self._collection)
        links = await session.scalars(query)
        return [OperationToQualificationTypeSchema.model_validate(obj=link) for link in links.all()]

    async def get_link_by_id(self, session: AsyncSession, link_id: int) -> OperationToQualificationTypeSchema:
        query = select(self._collection).where(self._collection.id == link_id)
        link = await session.scalar(query)
        if not link:
            raise OperationToQualificationTypeNotFound(_id=link_id)
        return OperationToQualificationTypeSchema.model_validate(obj=link)

    async def create_link(self, session: AsyncSession, link: OperationToQualificationTypeCreateUpdateSchema) -> OperationToQualificationTypeSchema:
        query = insert(self._collection).values(link.model_dump()).returning(self._collection)
        try:
            created_link = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise OperationToQualificationTypeAlreadyExists()
        return OperationToQualificationTypeSchema.model_validate(obj=created_link)

    async def update_link(self, session: AsyncSession, link_id: int, link: OperationToQualificationTypeCreateUpdateSchema) -> OperationToQualificationTypeSchema:
        query = update(self._collection).where(self._collection.id == link_id).values(link.model_dump()).returning(self._collection)
        updated_link = await session.scalar(query)
        if not updated_link:
            raise OperationToQualificationTypeNotFound(_id=link_id)
        return OperationToQualificationTypeSchema.model_validate(obj=updated_link)

    async def delete_link(self, session: AsyncSession, link_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == link_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise OperationToQualificationTypeNotFound(_id=link_id)
