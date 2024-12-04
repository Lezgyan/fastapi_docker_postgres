from sqlalchemy import select, delete, update
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


from project.core.exceptions import PositionNotFound, PositionAlreadyExists
from project.infrastructure.postgres.models import Position
from project.schemas.position import PositionSchema, PositionCreateUpdateSchema


class PositionRepository:
    _collection = Position

    async def get_all_positions(self, session: AsyncSession) -> list[PositionSchema]:
        query = select(self._collection)
        positions = await session.scalars(query)
        return [PositionSchema.model_validate(obj=position) for position in positions.all()]

    async def get_position_by_id(self, session: AsyncSession, position_id: int) -> PositionSchema:
        query = select(self._collection).where(self._collection.position_id == position_id)
        position = await session.scalar(query)
        if not position:
            raise PositionNotFound(_id=position_id)
        return PositionSchema.model_validate(obj=position)

    async def create_position(self, session: AsyncSession, position: PositionCreateUpdateSchema) -> PositionSchema:
        query = insert(self._collection).values(position.model_dump()).returning(self._collection)
        try:
            created_position = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise PositionAlreadyExists(name=position.name)
        return PositionSchema.model_validate(obj=created_position)

    async def update_position(self, session: AsyncSession, position_id: int, position: PositionCreateUpdateSchema) -> PositionSchema:
        query = update(self._collection).where(self._collection.position_id == position_id).values(position.model_dump()).returning(self._collection)
        updated_position = await session.scalar(query)
        if not updated_position:
            raise PositionNotFound(_id=position_id)
        return PositionSchema.model_validate(obj=updated_position)

    async def delete_position(self, session: AsyncSession, position_id: int) -> None:
        query = delete(self._collection).where(self._collection.position_id == position_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise PositionNotFound(_id=position_id)
