from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import DiseaseNotFound, DiseaseAlreadyExists
from project.infrastructure.postgres.models import Disease
from project.schemas.disease import DiseasesSchema, DiseasesCreateUpdateSchema


class DiseasesRepository:
    _collection = Disease

    async def get_all_diseases(self, session: AsyncSession) -> list[DiseasesSchema]:
        query = select(self._collection)
        diseases = await session.scalars(query)
        return [DiseasesSchema.model_validate(obj=disease) for disease in diseases.all()]

    async def get_disease_by_id(self, session: AsyncSession, disease_id: int) -> DiseasesSchema:
        query = select(self._collection).where(self._collection.disease_id == disease_id)
        disease = await session.scalar(query)
        if not disease:
            raise DiseaseNotFound(_id=disease_id)
        return DiseasesSchema.model_validate(obj=disease)

    async def create_disease(self, session: AsyncSession, disease: DiseasesCreateUpdateSchema) -> DiseasesSchema:
        query = insert(self._collection).values(disease.model_dump()).returning(self._collection)
        try:
            created_disease = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise DiseaseAlreadyExists(name=disease.name, icd_code=disease.icd_code)
        return DiseasesSchema.model_validate(obj=created_disease)

    async def update_disease(self, session: AsyncSession, disease_id: int, disease: DiseasesCreateUpdateSchema) -> DiseasesSchema:
        query = (
            update(self._collection)
            .where(self._collection.disease_id == disease_id)
            .values(disease.model_dump())
            .returning(self._collection)
        )
        updated_disease = await session.scalar(query)
        if not updated_disease:
            raise DiseaseNotFound(_id=disease_id)
        return DiseasesSchema.model_validate(obj=updated_disease)

    async def delete_disease(self, session: AsyncSession, disease_id: int) -> None:
        query = delete(self._collection).where(self._collection.disease_id == disease_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise DiseaseNotFound(_id=disease_id)
