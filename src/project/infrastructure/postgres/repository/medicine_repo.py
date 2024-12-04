
from sqlalchemy import delete, update, insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import MedicineNotFound, MedicineAlreadyExists
from project.infrastructure.postgres.models import Medicine
from project.schemas.medicine import MedicineSchema, MedicineCreateUpdateSchema


class MedicineRepository:
    _collection = Medicine

    async def get_all_medicine(self, session: AsyncSession) -> list[MedicineSchema]:
        query = select(self._collection)
        medicines = await session.scalars(query)
        return [MedicineSchema.model_validate(obj=medicine) for medicine in medicines.all()]

    async def get_medicine_by_id(self, session: AsyncSession, medicine_id: int) -> MedicineSchema:
        query = select(self._collection).where(self._collection.id == medicine_id)
        medicine = await session.scalar(query)
        if not medicine:
            raise MedicineNotFound(_id=medicine_id)
        return MedicineSchema.model_validate(obj=medicine)

    async def create_medicine(self, session: AsyncSession, medicine: MedicineCreateUpdateSchema) -> MedicineSchema:
        query = insert(self._collection).values(medicine.model_dump()).returning(self._collection)
        try:
            created_medicine = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise MedicineAlreadyExists(name=medicine.name)
        return MedicineSchema.model_validate(obj=created_medicine)

    async def update_medicine(self, session: AsyncSession, medicine_id: int, medicine: MedicineCreateUpdateSchema) -> MedicineSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == medicine_id)
            .values(medicine.model_dump())
            .returning(self._collection)
        )
        updated_medicine = await session.scalar(query)
        if not updated_medicine:
            raise MedicineNotFound(_id=medicine_id)
        return MedicineSchema.model_validate(obj=updated_medicine)

    async def delete_medicine(self, session: AsyncSession, medicine_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == medicine_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise MedicineNotFound(_id=medicine_id)
