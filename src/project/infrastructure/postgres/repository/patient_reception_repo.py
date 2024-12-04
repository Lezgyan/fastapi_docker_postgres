from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import PatientReceptionNotFound, PatientReceptionAlreadyExists
from project.infrastructure.postgres.models import PatientReception
from project.schemas.patient_reception import PatientReceptionSchema, PatientReceptionCreateUpdateSchema


class PatientReceptionRepository:
    _collection = PatientReception

    async def get_all_patient_receptions(self, session: AsyncSession) -> list[PatientReceptionSchema]:
        query = select(self._collection)
        receptions = await session.scalars(query)
        return [PatientReceptionSchema.model_validate(obj=reception) for reception in receptions.all()]

    async def get_patient_reception_by_id(self, session: AsyncSession, reception_id: int) -> PatientReceptionSchema:
        query = select(self._collection).where(self._collection.id == reception_id)
        reception = await session.scalar(query)
        if not reception:
            raise PatientReceptionNotFound(_id=reception_id)
        return PatientReceptionSchema.model_validate(obj=reception)

    async def create_patient_reception(self, session: AsyncSession, reception: PatientReceptionCreateUpdateSchema) -> PatientReceptionSchema:
        query = insert(self._collection).values(reception.model_dump()).returning(self._collection)
        try:
            created_reception = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise PatientReceptionAlreadyExists()
        return PatientReceptionSchema.model_validate(obj=created_reception)

    async def update_patient_reception(self, session: AsyncSession, reception_id: int, reception: PatientReceptionCreateUpdateSchema) -> PatientReceptionSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == reception_id)
            .values(reception.model_dump())
            .returning(self._collection)
        )
        updated_reception = await session.scalar(query)
        if not updated_reception:
            raise PatientReceptionNotFound(_id=reception_id)
        return PatientReceptionSchema.model_validate(obj=updated_reception)

    async def delete_patient_reception(self, session: AsyncSession, reception_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == reception_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise PatientReceptionNotFound(_id=reception_id)










