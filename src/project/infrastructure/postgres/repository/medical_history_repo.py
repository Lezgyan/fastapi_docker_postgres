from sqlalchemy import delete, update, insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import MedicalHistoryNotFound, MedicalHistoryAlreadyExists
from project.infrastructure.postgres.models import MedicalHistory
from project.schemas.medical_history import MedicalHistorySchema, MedicalHistoryCreateUpdateSchema


class MedicalHistoryRepository:
    _collection = MedicalHistory

    async def get_all_medical_histories(self, session: AsyncSession) -> list[MedicalHistorySchema]:
        query = select(self._collection)
        histories = await session.scalars(query)
        return [MedicalHistorySchema.model_validate(obj=history) for history in histories.all()]

    async def get_medical_history_by_id(self, session: AsyncSession, history_id: int) -> MedicalHistorySchema:
        query = select(self._collection).where(self._collection.history_id == history_id)
        history = await session.scalar(query)
        if not history:
            raise MedicalHistoryNotFound(_id=history_id)
        return MedicalHistorySchema.model_validate(obj=history)

    async def create_medical_history(self, session: AsyncSession, history: MedicalHistoryCreateUpdateSchema) -> MedicalHistorySchema:
        query = insert(self._collection).values(history.model_dump()).returning(self._collection)
        try:
            created_history = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise MedicalHistoryAlreadyExists(patient_id=history.patient_id, disease_id=history.disease_id)
        return MedicalHistorySchema.model_validate(obj=created_history)

    async def update_medical_history(self, session: AsyncSession, history_id: int, history: MedicalHistoryCreateUpdateSchema) -> MedicalHistorySchema:
        query = (
            update(self._collection)
            .where(self._collection.history_id == history_id)
            .values(history.model_dump())
            .returning(self._collection)
        )
        updated_history = await session.scalar(query)
        if not updated_history:
            raise MedicalHistoryNotFound(_id=history_id)
        return MedicalHistorySchema.model_validate(obj=updated_history)

    async def delete_medical_history(self, session: AsyncSession, history_id: int) -> None:
        query = delete(self._collection).where(self._collection.history_id == history_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise MedicalHistoryNotFound(_id=history_id)
