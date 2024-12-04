from typing import Type

from sqlalchemy import insert, update, delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import DoctorNotFound, DoctorAlreadyExists
from project.infrastructure.postgres.models import Doctor
from project.schemas.doctors import DoctorsSchema, DoctorsCreateUpdateSchema


#
# class DoctorsRepository:
#     _collection: Type[Doctor] = Doctor
#
#     async def get_all_doctors(self, session: AsyncSession) -> list[DoctorsSchema]:
#         query = select(self._collection)
#         doctors = await session.scalars(query)
#         return [DoctorsSchema.model_validate(obj=doctor) for doctor in doctors.all()]
#
#     async def get_doctor_by_id(self, session: AsyncSession, doctor_id: int) -> DoctorsSchema:
#         query = select(Doctor).where(self._collection.doctor_id == doctor_id)
#         doctor = await session.scalar(query)
#         if not doctor:
#             raise DoctorNotFound(_id=doctor_id)
#         return DoctorsSchema.model_validate(obj=doctor)
#
#     async def create_doctor(self, session: AsyncSession, doctor: DoctorsCreateUpdateSchema) -> DoctorsSchema:
#         query = insert(self._collection).values(doctor.model_dump()).returning(self._collection)
#         try:
#             created_doctor = await session.scalar(query)
#             await session.flush()
#         except IntegrityError:
#             raise DoctorAlreadyExists(full_name=doctor.full_name)
#         return DoctorsSchema.model_validate(obj=created_doctor)
#
#     async def update_doctor(self, session: AsyncSession, doctor_id: int, doctor: DoctorsCreateUpdateSchema) -> DoctorsSchema:
#         query = (
#             update(self._collection)
#             .where(self._collection.doctor_id == doctor_id)
#             .values(doctor.model_dump())
#             .returning(self._collection)
#         )
#         updated_doctor = await session.scalar(query)
#         if not updated_doctor:
#             raise DoctorNotFound(_id=doctor_id)
#         return DoctorsSchema.model_validate(obj=updated_doctor)
#
#     async def delete_doctor(self, session: AsyncSession, doctor_id: int) -> None:
#         query = delete(self._collection).where(self._collection.doctor_id == doctor_id)
#         result = await session.execute(query)
#         if not result.rowcount:
#             raise DoctorNotFound(_id=doctor_id)


class DoctorsRepository:
    _collection: Type[Doctor] = Doctor

    async def get_all_doctors(self, session: AsyncSession) -> list[DoctorsSchema]:
        """Fetch all doctors."""
        query = select(self._collection)
        result = await session.execute(query)
        doctors = result.scalars().all()
        return [DoctorsSchema.model_validate(obj=doctor) for doctor in doctors]

    async def get_doctor_by_id(self, session: AsyncSession, doctor_id: int) -> DoctorsSchema:
        """Fetch a doctor by ID."""
        query = select(self._collection).where(self._collection.doctor_id == doctor_id)
        result = await session.execute(query)
        doctor = result.scalar_one_or_none()
        if not doctor:
            raise DoctorNotFound(_id=doctor_id)
        return DoctorsSchema.model_validate(obj=doctor)

    async def create_doctor(self, session: AsyncSession, doctor: DoctorsCreateUpdateSchema) -> DoctorsSchema:
        """Create a new doctor."""
        query = insert(self._collection).values(**doctor.model_dump()).returning(self._collection)
        try:
            result = await session.execute(query)
            created_doctor = result.scalar_one()
            await session.commit()
        except IntegrityError as e:
            await session.rollback()
            raise DoctorAlreadyExists(full_name=doctor.full_name) from e
        return DoctorsSchema.model_validate(obj=created_doctor)

    async def update_doctor(self, session: AsyncSession, doctor_id: int,
                            doctor: DoctorsCreateUpdateSchema) -> DoctorsSchema:
        """Update a doctor's information."""
        query = (
            update(self._collection)
            .where(self._collection.doctor_id == doctor_id)
            .values(**doctor.model_dump())
            .returning(self._collection)
        )
        result = await session.execute(query)
        updated_doctor = result.scalar_one_or_none()
        if not updated_doctor:
            await session.rollback()
            raise DoctorNotFound(_id=doctor_id)
        await session.commit()
        return DoctorsSchema.model_validate(obj=updated_doctor)

    async def delete_doctor(self, session: AsyncSession, doctor_id: int) -> None:
        """Delete a doctor by ID."""
        query = delete(self._collection).where(self._collection.doctor_id == doctor_id)
        result = await session.execute(query)
        if result.rowcount == 0:
            await session.rollback()
            raise DoctorNotFound(_id=doctor_id)
        await session.commit()
