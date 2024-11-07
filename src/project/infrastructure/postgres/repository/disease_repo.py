from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, insert, update, delete

from project.core.config import settings

from project.infrastructure.postgres.models import Disease
from project.schemas.disease import DiseaseSchema


class DiseaseRepository:
    _collection: Type[Disease] = Disease

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
            disease: DiseaseSchema,
    ) -> DiseaseSchema:
        result = await session.scalar(insert(Disease).returning(Disease), [disease.dict()])

        return DiseaseSchema.model_validate(obj=result)

    async def update_disease(
            self,
            session: AsyncSession,
            disease: DiseaseSchema,
    ) -> DiseaseSchema:
        query = (update(Disease)
                 .where(Disease.disease_id == disease.disease_id)
                 .values(**disease.dict())
                 .returning(Disease))
        result = await session.scalar(query)

        return DiseaseSchema.model_validate(obj=result)

    async def delete_disease(
            self,
            session: AsyncSession,
            disease: DiseaseSchema,
    ):
        await session.execute(delete(Disease)
                             .where(Disease.disease_id == disease.disease_id))
