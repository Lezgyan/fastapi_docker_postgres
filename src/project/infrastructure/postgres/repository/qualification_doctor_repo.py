from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from project.core.exceptions import QualificationDoctorNotFound, QualificationDoctorAlreadyExists
from project.infrastructure.postgres.models import QualificationDoctor
from project.schemas.qualification_doctor import QualificationDoctorSchema, QualificationDoctorCreateUpdateSchema


class QualificationDoctorRepository:
    _collection = QualificationDoctor

    async def get_all_qualification_doctors(self, session: AsyncSession) -> list[QualificationDoctorSchema]:
        query = select(self._collection)
        qualification_doctors = await session.scalars(query)
        return [QualificationDoctorSchema.model_validate(obj=qd) for qd in qualification_doctors.all()]

    async def get_qualification_doctor_by_id(self, session: AsyncSession, qd_id: int) -> QualificationDoctorSchema:
        query = select(self._collection).where(self._collection.id == qd_id)
        qualification_doctor = await session.scalar(query)
        if not qualification_doctor:
            raise QualificationDoctorNotFound(_id=qd_id)
        return QualificationDoctorSchema.model_validate(obj=qualification_doctor)

    async def create_qualification_doctor(self, session: AsyncSession, qd: QualificationDoctorCreateUpdateSchema) -> QualificationDoctorSchema:
        query = insert(self._collection).values(qd.model_dump()).returning(self._collection)
        try:
            created_qd = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise QualificationDoctorAlreadyExists(doctor_id=qd.doctor_id, qualification_id=qd.qualification_id)
        return QualificationDoctorSchema.model_validate(obj=created_qd)

    async def update_qualification_doctor(self, session: AsyncSession, qd_id: int, qd: QualificationDoctorCreateUpdateSchema) -> QualificationDoctorSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == qd_id)
            .values(qd.model_dump())
            .returning(self._collection)
        )
        updated_qd = await session.scalar(query)
        if not updated_qd:
            raise QualificationDoctorNotFound(_id=qd_id)
        return QualificationDoctorSchema.model_validate(obj=updated_qd)

    async def delete_qualification_doctor(self, session: AsyncSession, qd_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == qd_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise QualificationDoctorNotFound(_id=qd_id)
