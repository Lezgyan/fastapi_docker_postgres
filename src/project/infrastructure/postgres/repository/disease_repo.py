from typing import Type, Final

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, insert, update, delete

from project.core.config import settings

from project.infrastructure.postgres.models import Disease
from project.schemas.disease import DiseaseSchema, DiseaseCreateUpdateSchema
from project.core.exceptions import EntityNotFound


class DiseaseRepository:
    _collection: Type[Disease] = Disease
    _entity: Final[str] = 'Disease'

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_deseases(
            self,
            session: AsyncSession,
    ) -> list[DiseaseSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.diseases;"

        diseases = await session.execute(text(query))

        return [DiseaseSchema.model_validate(obj=disease) for disease in diseases.mappings().all()]

    async def save_disease(
            self,
            session: AsyncSession,
            disease: DiseaseCreateUpdateSchema,
    ) -> DiseaseSchema:
        query = insert(self._collection).values(disease.model_dump()).returning(self._collection)

        result = await session.scalar(query)

        return DiseaseSchema.model_validate(obj=result)

    async def update_disease(
            self,
            session: AsyncSession,
            disease: DiseaseCreateUpdateSchema,
    ) -> DiseaseSchema:
        query = (
            update(self._collection)
            .where(Disease.disease_id == disease.disease_id)
            .values(**disease.model_dump())
            .returning(self._collection)
        )
        result = await session.scalar(query)
        if not result:
            raise EntityNotFound(entity=self._entity, _id=disease_id)

        return DiseaseSchema.model_validate(obj=result)

    async def delete_disease(
            self,
            session: AsyncSession,
            disease_id: int,
    ) -> None:
        query = delete(self._collection).where(self._collection.disease_id == disease_id)

        result = await session.execute(query)
        if result.rowcount == 0:
            raise EntityNotFound(entity=self._entity, _id=disease_id)

        await session.flush()
