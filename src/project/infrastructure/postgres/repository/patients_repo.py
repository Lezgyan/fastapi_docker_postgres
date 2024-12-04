from sqlalchemy import delete, update, insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import PatientNotFound, PatientAlreadyExists
from project.infrastructure.postgres.models import Patient
from project.schemas.patients import PatientsSchema, PatientsCreateUpdateSchema


class PatientsRepository:
    _collection = Patient

    async def get_all_patients(self, session: AsyncSession) -> list[PatientsSchema]:
        query = select(self._collection)
        patients = await session.scalars(query)
        return [PatientsSchema.model_validate(obj=patient) for patient in patients.all()]

    async def get_patient_by_id(self, session: AsyncSession, patient_id: int) -> PatientsSchema:
        query = select(self._collection).where(self._collection.patient_id == patient_id)
        patient = await session.scalar(query)
        if not patient:
            raise PatientNotFound(_id=patient_id)
        return PatientsSchema.model_validate(obj=patient)

    async def create_patient(self, session: AsyncSession, patient: PatientsCreateUpdateSchema) -> PatientsSchema:
        query = insert(self._collection).values(patient.model_dump()).returning(self._collection)
        try:
            created_patient = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise PatientAlreadyExists(snils=patient.snils, medical_policy=patient.medical_policy)
        return PatientsSchema.model_validate(obj=created_patient)

    async def update_patient(self, session: AsyncSession, patient_id: int, patient: PatientsCreateUpdateSchema) -> PatientsSchema:
        query = (
            update(self._collection)
            .where(self._collection.patient_id == patient_id)
            .values(patient.model_dump())
            .returning(self._collection)
        )
        updated_patient = await session.scalar(query)
        if not updated_patient:
            raise PatientNotFound(_id=patient_id)
        return PatientsSchema.model_validate(obj=updated_patient)

    async def delete_patient(self, session: AsyncSession, patient_id: int) -> None:
        query = delete(self._collection).where(self._collection.patient_id == patient_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise PatientNotFound(_id=patient_id)
