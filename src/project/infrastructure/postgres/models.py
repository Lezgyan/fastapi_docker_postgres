from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from project.infrastructure.postgres.database import Base


class Disease(Base):
    __tablename__ = "diseases"

    disease_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    icd_code: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=True)


#
class Position(Base):
    __tablename__ = "positions"

    position_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)


#
class Ward(Base):
    __tablename__ = "ward"

    id: Mapped[int] = mapped_column(primary_key=True)
    count_bunk: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.department_id"), nullable=False)


#
class OperationToQualificationType(Base):
    __tablename__ = "operation_to_qualification_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    operation_type_id: Mapped[int] = mapped_column(ForeignKey("operation_types.operation_type_id"), nullable=False)
    qualification_type_id: Mapped[int] = mapped_column(ForeignKey("qualification_type.id"), nullable=False)


#
class CourseOfTreatment(Base):
    __tablename__ = "course_of_treatment"

    id: Mapped[int] = mapped_column(primary_key=True)
    history_id: Mapped[int] = mapped_column(ForeignKey("medical_history.history_id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    receipt_date: Mapped[datetime] = mapped_column(nullable=False)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.doctor_id"), nullable=False)

# #
class Doctor(Base):
    __tablename__ = "doctors"

    doctor_id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(nullable=False)
    position_id: Mapped[int] = mapped_column(ForeignKey("positions.position_id"), nullable=False)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.department_id"), nullable=False)


#
class Medicine(Base):
    __tablename__ = "medicine"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=False)


#
#
class MedicalHistory(Base):
    __tablename__ = "medical_history"

    history_id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.patient_id"), nullable=False)
    disease_id: Mapped[int] = mapped_column(ForeignKey("diseases.disease_id"), nullable=False)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.doctor_id"), nullable=False)
    admission_date: Mapped[datetime] = mapped_column(nullable=False)
    discharge_date: Mapped[datetime] = mapped_column(nullable=True)
    notes: Mapped[str] = mapped_column(nullable=True)
    ward_id: Mapped[int] = mapped_column(ForeignKey("ward.id"), nullable=False)


#
class OperationType(Base):
    __tablename__ = "operation_types"

    operation_type_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)


#
class PatientReception(Base):
    __tablename__ = "patient_reception"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    course_of_treatment_id: Mapped[int] = mapped_column(ForeignKey("course_of_treatment.id"), nullable=False)
    medication_id: Mapped[int] = mapped_column(ForeignKey("medicine.id"), nullable=False)


#

class QualificationDoctor(Base):
    __tablename__ = "qualification_doctor"

    id: Mapped[int] = mapped_column(primary_key=True)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.doctor_id"), nullable=False)
    qualification_id: Mapped[int] = mapped_column(ForeignKey("qualification_type.id"), nullable=False)

#
class Department(Base):
    __tablename__ = "departments"

    department_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)


#
#
class Patient(Base):
    __tablename__ = "patients"

    patient_id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(nullable=False)
    date_of_birth: Mapped[datetime] = mapped_column(nullable=False)
    snils: Mapped[str] = mapped_column(nullable=False, unique=True)
    medical_policy: Mapped[str] = mapped_column(nullable=False, unique=True)


#
#
class Operation(Base):
    __tablename__ = "operations"

    operation_id: Mapped[int] = mapped_column(primary_key=True)
    history_id: Mapped[int] = mapped_column(ForeignKey("medical_history.history_id"), nullable=False)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.doctor_id"), nullable=False)
    operation_type_id: Mapped[int] = mapped_column(ForeignKey("operation_types.operation_type_id"), nullable=False)
    operation_date: Mapped[datetime] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)

#
#
class QualificationType(Base):
    __tablename__ = "qualification_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
