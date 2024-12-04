from sqlalchemy import delete, update, insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import OperationTypeNotFound, OperationTypeAlreadyExists
from project.infrastructure.postgres.models import OperationType
from project.schemas.operation_types import OperationTypesSchema, OperationTypesCreateUpdateSchema


class OperationTypesRepository:
    _collection = OperationType

    async def get_all_operation_types(self, session: AsyncSession) -> list[OperationTypesSchema]:
        query = select(self._collection)
        operation_types = await session.scalars(query)
        return [OperationTypesSchema.model_validate(obj=op_type) for op_type in operation_types.all()]

    async def get_operation_type_by_id(self, session: AsyncSession, operation_type_id: int) -> OperationTypesSchema:
        query = select(self._collection).where(self._collection.operation_type_id == operation_type_id)
        operation_type = await session.scalar(query)
        if not operation_type:
            raise OperationTypeNotFound(_id=operation_type_id)
        return OperationTypesSchema.model_validate(obj=operation_type)

    async def create_operation_type(self, session: AsyncSession, operation_type: OperationTypesCreateUpdateSchema) -> OperationTypesSchema:
        query = insert(self._collection).values(operation_type.model_dump()).returning(self._collection)
        try:
            created_operation_type = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise OperationTypeAlreadyExists(name=operation_type.name)
        return OperationTypesSchema.model_validate(obj=created_operation_type)

    async def update_operation_type(self, session: AsyncSession, operation_type_id: int, operation_type: OperationTypesCreateUpdateSchema) -> OperationTypesSchema:
        query = (
            update(self._collection)
            .where(self._collection.operation_type_id == operation_type_id)
            .values(operation_type.model_dump())
            .returning(self._collection)
        )
        updated_operation_type = await session.scalar(query)
        if not updated_operation_type:
            raise OperationTypeNotFound(_id=operation_type_id)
        return OperationTypesSchema.model_validate(obj=updated_operation_type)

    async def delete_operation_type(self, session: AsyncSession, operation_type_id: int) -> None:
        query = delete(self._collection).where(self._collection.operation_type_id == operation_type_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise OperationTypeNotFound(_id=operation_type_id)
