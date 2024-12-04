from sqlalchemy import delete, update, insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import OperationNotFound, OperationAlreadyExists
from project.infrastructure.postgres.models import Operation

from project.schemas.operations import OperationsSchema, OperationsCreateUpdateSchema


class OperationsRepository:
    _collection = Operation

    async def get_all_operations(self, session: AsyncSession) -> list[OperationsSchema]:
        query = select(self._collection)
        operations = await session.scalars(query)
        return [OperationsSchema.model_validate(obj=operation) for operation in operations.all()]

    async def get_operation_by_id(self, session: AsyncSession, operation_id: int) -> OperationsSchema:
        query = select(self._collection).where(self._collection.operation_id == operation_id)
        operation = await session.scalar(query)
        if not operation:
            raise OperationNotFound(_id=operation_id)
        return OperationsSchema.model_validate(obj=operation)

    async def create_operation(self, session: AsyncSession, operation: OperationsCreateUpdateSchema) -> OperationsSchema:
        query = insert(self._collection).values(operation.model_dump()).returning(self._collection)
        try:
            created_operation = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise OperationAlreadyExists(history_id=operation.history_id, operation_date=operation.operation_date)
        return OperationsSchema.model_validate(obj=created_operation)

    async def update_operation(self, session: AsyncSession, operation_id: int, operation: OperationsCreateUpdateSchema) -> OperationsSchema:
        query = (
            update(self._collection)
            .where(self._collection.operation_id == operation_id)
            .values(operation.model_dump())
            .returning(self._collection)
        )
        updated_operation = await session.scalar(query)
        if not updated_operation:
            raise OperationNotFound(_id=operation_id)
        return OperationsSchema.model_validate(obj=updated_operation)

    async def delete_operation(self, session: AsyncSession, operation_id: int) -> None:
        query = delete(self._collection).where(self._collection.operation_id == operation_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise OperationNotFound(_id=operation_id)


