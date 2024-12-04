from sqlalchemy import select, delete, update, insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import WardNotFound, WardAlreadyExists
from project.infrastructure.postgres.models import Ward
from project.schemas.ward import WardSchema, WardCreateUpdateSchema


class WardRepository:
    _collection = Ward

    async def get_all_wards(self, session: AsyncSession) -> list[WardSchema]:
        query = select(self._collection)
        wards = await session.scalars(query)
        return [WardSchema.model_validate(obj=ward) for ward in wards.all()]

    async def get_ward_by_id(self, session: AsyncSession, ward_id: int) -> WardSchema:
        query = select(self._collection).where(self._collection.id == ward_id)
        ward = await session.scalar(query)
        if not ward:
            raise WardNotFound(_id=ward_id)
        return WardSchema.model_validate(obj=ward)

    async def create_ward(self, session: AsyncSession, ward: WardCreateUpdateSchema) -> WardSchema:
        query = insert(self._collection).values(ward.model_dump()).returning(self._collection)
        try:
            created_ward = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise WardAlreadyExists(name=ward.name)
        return WardSchema.model_validate(obj=created_ward)

    async def update_ward(self, session: AsyncSession, ward_id: int, ward: WardCreateUpdateSchema) -> WardSchema:
        query = update(self._collection).where(self._collection.id == ward_id).values(ward.model_dump()).returning(self._collection)
        updated_ward = await session.scalar(query)
        if not updated_ward:
            raise WardNotFound(_id=ward_id)
        return WardSchema.model_validate(obj=updated_ward)

    async def delete_ward(self, session: AsyncSession, ward_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == ward_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise WardNotFound(_id=ward_id)
