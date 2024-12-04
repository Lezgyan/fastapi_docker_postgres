from project.infrastructure.postgres.database import PostgresDatabase
from project.infrastructure.postgres.models import OperationToQualificationType, OperationType, QualificationType

from project.infrastructure.postgres.repository.course_of_treatment_repo import CourseOfTreatmentRepository
from project.infrastructure.postgres.repository.departments_repo import DepartmentsRepository
from project.infrastructure.postgres.repository.diseases_repo import DiseasesRepository
from project.infrastructure.postgres.repository.doctors_repo import DoctorsRepository
from project.infrastructure.postgres.repository.medical_history_repo import MedicalHistoryRepository
from project.infrastructure.postgres.repository.medicine_repo import MedicineRepository
from project.infrastructure.postgres.repository.operations_repo import OperationsRepository
from project.infrastructure.postgres.repository.patient_reception_repo import PatientReceptionRepository
from project.infrastructure.postgres.repository.patients_repo import PatientsRepository
from project.infrastructure.postgres.repository.position_repo import PositionRepository
from project.infrastructure.postgres.repository.qualification_doctor_repo import QualificationDoctorRepository
from project.infrastructure.postgres.repository.ward_repo import WardRepository

course_of_treatment_repo = CourseOfTreatmentRepository()
departments_repo = DepartmentsRepository()
doctors_repo = DoctorsRepository()
medical_history_repo = MedicalHistoryRepository()
medicine_repo = MedicineRepository()


operation_to_qualification_type_repo = OperationToQualificationType()
operation_types_repo = OperationType()
operations_repo = OperationsRepository()
patient_reception_repo = PatientReceptionRepository()
patients_repo = PatientsRepository()
position_repo = PositionRepository()
qualification_doctor_repo = QualificationDoctorRepository()
qualifications_type_repo = QualificationType()
ward_repo = WardRepository()
diseases_repo = DiseasesRepository()
database = PostgresDatabase()
