from fastapi import APIRouter, status, HTTPException

from project.api.depends import database, diseases_repo, operation_to_qualification_type_repo, position_repo, \
    medicine_repo, operation_types_repo, departments_repo, patients_repo, ward_repo, doctors_repo, \
    medical_history_repo, course_of_treatment_repo, operations_repo, patient_reception_repo, \
    qualification_doctor_repo
from project.core.exceptions import DiseaseNotFound, DiseaseAlreadyExists, OperationToQualificationTypeNotFound, \
    OperationToQualificationTypeAlreadyExists, PositionNotFound, PositionAlreadyExists, MedicineNotFound, \
    MedicineAlreadyExists, OperationTypeNotFound, \
    OperationTypeAlreadyExists, DepartmentNotFound, DepartmentAlreadyExists, PatientNotFound, PatientAlreadyExists, \
    WardNotFound, WardAlreadyExists, DoctorNotFound, DoctorAlreadyExists, MedicalHistoryNotFound, \
    MedicalHistoryAlreadyExists, CourseOfTreatmentNotFound, CourseOfTreatmentAlreadyExists, OperationNotFound, \
    OperationAlreadyExists, PatientReceptionNotFound, PatientReceptionAlreadyExists, QualificationDoctorNotFound, \
    QualificationDoctorAlreadyExists
from project.schemas.course_of_treatment import CourseOfTreatmentCreateUpdateSchema, CourseOfTreatmentSchema

from project.schemas.departments import DepartmentsCreateUpdateSchema, DepartmentsSchema

from project.schemas.disease import DiseasesSchema, DiseasesCreateUpdateSchema
from project.schemas.doctors import DoctorsCreateUpdateSchema, DoctorsSchema
from project.schemas.healthcheck import HealthCheckSchema
from project.schemas.medical_history import MedicalHistoryCreateUpdateSchema, MedicalHistorySchema
from project.schemas.medicine import MedicineCreateUpdateSchema, MedicineSchema
from project.schemas.operation_to_qualification_type import OperationToQualificationTypeSchema, \
    OperationToQualificationTypeCreateUpdateSchema
from project.schemas.operation_types import OperationTypesCreateUpdateSchema, OperationTypesSchema
from project.schemas.operations import OperationsSchema, OperationsCreateUpdateSchema
from project.schemas.patient_reception import PatientReceptionCreateUpdateSchema, PatientReceptionSchema

from project.schemas.patients import PatientsCreateUpdateSchema, PatientsSchema
from project.schemas.position import PositionSchema, PositionCreateUpdateSchema
from project.schemas.qualification_doctor import QualificationDoctorSchema, QualificationDoctorCreateUpdateSchema
from project.schemas.ward import WardCreateUpdateSchema, WardSchema

router = APIRouter()


@router.get("/healthcheck", response_model=HealthCheckSchema, status_code=status.HTTP_200_OK)
async def check_health() -> HealthCheckSchema:
    async with database.session() as session:
        db_is_ok = await diseases_repo.check_connection(session=session)

    return HealthCheckSchema(
        db_is_ok=db_is_ok,
    )


@router.get("/all_diseases", response_model=list[DiseasesSchema], status_code=status.HTTP_200_OK)
async def get_all_diseases() -> list[DiseasesSchema]:
    async with database.session() as session:
        all_diseases = await diseases_repo.get_all_diseases(session=session)

    return all_diseases


@router.get("/disease/{disease_id}", response_model=DiseasesSchema, status_code=status.HTTP_200_OK)
async def get_disease_by_id(disease_id: int) -> DiseasesSchema:
    try:
        async with database.session() as session:
            disease = await diseases_repo.get_disease_by_id(session=session, disease_id=disease_id)
    except DiseaseNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return disease


@router.post("/add_disease", response_model=DiseasesSchema, status_code=status.HTTP_201_CREATED)
async def add_disease(disease_dto: DiseasesCreateUpdateSchema) -> DiseasesSchema:
    try:
        async with database.session() as session:
            new_disease = await diseases_repo.create_disease(session=session, disease=disease_dto)
    except DiseaseAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_disease


@router.put("/update_disease/{disease_id}", response_model=DiseasesSchema, status_code=status.HTTP_200_OK)
async def update_disease(disease_id: int, disease_dto: DiseasesCreateUpdateSchema) -> DiseasesSchema:
    try:
        async with database.session() as session:
            updated_disease = await diseases_repo.update_disease(
                session=session, disease_id=disease_id, disease=disease_dto
            )
    except DiseaseNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_disease


@router.delete("/delete_disease/{disease_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_disease(disease_id: int) -> None:
    try:
        async with database.session() as session:
            await diseases_repo.delete_disease(session=session, disease_id=disease_id)
    except DiseaseNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)


#
#
#
#
#

@router.get("/all_courses", response_model=list[CourseOfTreatmentSchema], status_code=status.HTTP_200_OK)
async def get_all_courses() -> list[CourseOfTreatmentSchema]:
    async with database.session() as session:
        all_courses = await course_of_treatment_repo.get_all_courses(session=session)

    return all_courses


@router.get("/course/{course_id}", response_model=CourseOfTreatmentSchema, status_code=status.HTTP_200_OK)
async def get_course_by_id(course_id: int) -> CourseOfTreatmentSchema:
    try:
        async with database.session() as session:
            course = await course_of_treatment_repo.get_course_by_id(session=session, course_id=course_id)
    except CourseOfTreatmentNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return course


@router.post("/add_course", response_model=CourseOfTreatmentSchema, status_code=status.HTTP_201_CREATED)
async def add_course(course_dto: CourseOfTreatmentCreateUpdateSchema) -> CourseOfTreatmentSchema:
    try:
        async with database.session() as session:
            new_course = await course_of_treatment_repo.create_course(session=session, course=course_dto)
    except CourseOfTreatmentAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_course


@router.put("/update_course/{course_id}", response_model=CourseOfTreatmentSchema, status_code=status.HTTP_200_OK)
async def update_course(course_id: int, course_dto: CourseOfTreatmentCreateUpdateSchema) -> CourseOfTreatmentSchema:
    try:
        async with database.session() as session:
            updated_course = await course_of_treatment_repo.update_course(session=session, course_id=course_id,
                                                                          course=course_dto)
    except CourseOfTreatmentNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_course


@router.delete("/delete_course/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int) -> None:
    try:
        async with database.session() as session:
            await course_of_treatment_repo.delete_course(session=session, course_id=course_id)
    except CourseOfTreatmentNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

#
#
#
#
#
@router.get("/all_departments", response_model=list[DepartmentsSchema], status_code=status.HTTP_200_OK)
async def get_all_departments() -> list[DepartmentsSchema]:
    async with database.session() as session:
        all_departments = await departments_repo.get_all_departments(session=session)

    return all_departments


@router.get("/department/{department_id}", response_model=DepartmentsSchema, status_code=status.HTTP_200_OK)
async def get_department_by_id(department_id: int) -> DepartmentsSchema:
    try:
        async with database.session() as session:
            department = await departments_repo.get_department_by_id(session=session, department_id=department_id)
    except DepartmentNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return department


@router.post("/add_department", response_model=DepartmentsSchema, status_code=status.HTTP_201_CREATED)
async def add_department(department_dto: DepartmentsCreateUpdateSchema) -> DepartmentsSchema:
    try:
        async with database.session() as session:
            new_department = await departments_repo.create_department(session=session, department=department_dto)
    except DepartmentAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_department


@router.put("/update_department/{department_id}", response_model=DepartmentsSchema, status_code=status.HTTP_200_OK)
async def update_department(department_id: int, department_dto: DepartmentsCreateUpdateSchema) -> DepartmentsSchema:
    try:
        async with database.session() as session:
            updated_department = await departments_repo.update_department(
                session=session, department_id=department_id, department=department_dto
            )
    except DepartmentNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_department


@router.delete("/delete_department/{department_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_department(department_id: int) -> None:
    try:
        async with database.session() as session:
            await departments_repo.delete_department(session=session, department_id=department_id)
    except DepartmentNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
# #
# #
# #
# #
# #
# #
@router.get("/all_doctors", response_model=list[DoctorsSchema], status_code=status.HTTP_200_OK)
async def get_all_doctors() -> list[DoctorsSchema]:
    async with database.session() as session:
        all_doctors = await doctors_repo.get_all_doctors(session=session)

    return all_doctors


@router.get("/doctor/{doctor_id}", response_model=DoctorsSchema, status_code=status.HTTP_200_OK)
async def get_doctor_by_id(doctor_id: int) -> DoctorsSchema:
    try:
        async with database.session() as session:
            doctor = await doctors_repo.get_doctor_by_id(session=session, doctor_id=doctor_id)
    except DoctorNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return doctor


@router.post("/add_doctor", response_model=DoctorsSchema, status_code=status.HTTP_201_CREATED)
async def add_doctor(doctor_dto: DoctorsCreateUpdateSchema) -> DoctorsSchema:
    try:
        async with database.session() as session:
            new_doctor = await doctors_repo.create_doctor(session=session, doctor=doctor_dto)
    except DoctorAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_doctor


@router.put("/update_doctor/{doctor_id}", response_model=DoctorsSchema, status_code=status.HTTP_200_OK)
async def update_doctor(doctor_id: int, doctor_dto: DoctorsCreateUpdateSchema) -> DoctorsSchema:
    try:
        async with database.session() as session:
            updated_doctor = await doctors_repo.update_doctor(
                session=session, doctor_id=doctor_id, doctor=doctor_dto
            )
    except DoctorNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_doctor


@router.delete("/delete_doctor/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_doctor(doctor_id: int) -> None:
    try:
        async with database.session() as session:
            await doctors_repo.delete_doctor(session=session, doctor_id=doctor_id)
    except DoctorNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)


#
#
#
#
#
@router.get("/all_medical_histories", response_model=list[MedicalHistorySchema], status_code=status.HTTP_200_OK)
async def get_all_medical_histories() -> list[MedicalHistorySchema]:
    async with database.session() as session:
        all_histories = await medical_history_repo.get_all_medical_histories(session=session)

    return all_histories


@router.get("/medical_history/{history_id}", response_model=MedicalHistorySchema, status_code=status.HTTP_200_OK)
async def get_medical_history_by_id(history_id: int) -> MedicalHistorySchema:
    try:
        async with database.session() as session:
            history = await medical_history_repo.get_medical_history_by_id(session=session, history_id=history_id)
    except MedicalHistoryNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return history


@router.post("/add_medical_history", response_model=MedicalHistorySchema, status_code=status.HTTP_201_CREATED)
async def add_medical_history(history_dto: MedicalHistoryCreateUpdateSchema) -> MedicalHistorySchema:
    try:
        async with database.session() as session:
            new_history = await medical_history_repo.create_medical_history(session=session, history=history_dto)
    except MedicalHistoryAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_history


@router.put("/update_medical_history/{history_id}", response_model=MedicalHistorySchema, status_code=status.HTTP_200_OK)
async def update_medical_history(history_id: int, history_dto: MedicalHistoryCreateUpdateSchema) -> MedicalHistorySchema:
    try:
        async with database.session() as session:
            updated_history = await medical_history_repo.update_medical_history(
                session=session, history_id=history_id, history=history_dto
            )
    except MedicalHistoryNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_history


@router.delete("/delete_medical_history/{history_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_medical_history(history_id: int) -> None:
    try:
        async with database.session() as session:
            await medical_history_repo.delete_medical_history(session=session, history_id=history_id)
    except MedicalHistoryNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

#
#
#
#
#
#
#
@router.get("/all_medicine", response_model=list[MedicineSchema], status_code=status.HTTP_200_OK)
async def get_all_medicine() -> list[MedicineSchema]:
    async with database.session() as session:
        all_medicine = await medicine_repo.get_all_medicine(session=session)

    return all_medicine


@router.get("/medicine/{medicine_id}", response_model=MedicineSchema, status_code=status.HTTP_200_OK)
async def get_medicine_by_id(medicine_id: int) -> MedicineSchema:
    try:
        async with database.session() as session:
            medicine = await medicine_repo.get_medicine_by_id(session=session, medicine_id=medicine_id)
    except MedicineNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return medicine


@router.post("/add_medicine", response_model=MedicineSchema, status_code=status.HTTP_201_CREATED)
async def add_medicine(medicine_dto: MedicineCreateUpdateSchema) -> MedicineSchema:
    try:
        async with database.session() as session:
            new_medicine = await medicine_repo.create_medicine(session=session, medicine=medicine_dto)
    except MedicineAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_medicine


@router.put("/update_medicine/{medicine_id}", response_model=MedicineSchema, status_code=status.HTTP_200_OK)
async def update_medicine(medicine_id: int, medicine_dto: MedicineCreateUpdateSchema) -> MedicineSchema:
    try:
        async with database.session() as session:
            updated_medicine = await medicine_repo.update_medicine(
                session=session, medicine_id=medicine_id, medicine=medicine_dto
            )
    except MedicineNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_medicine


@router.delete("/delete_medicine/{medicine_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_medicine(medicine_id: int) -> None:
    try:
        async with database.session() as session:
            await medicine_repo.delete_medicine(session=session, medicine_id=medicine_id)
    except MedicineNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
#
#
#
#
#
@router.get(
    "/all_operation_to_qualification_types",
    response_model=list[OperationToQualificationTypeSchema],
    status_code=status.HTTP_200_OK,
)
async def get_all_operation_to_qualification_types() -> list[OperationToQualificationTypeSchema]:
    async with database.session() as session:
        all_links = await operation_to_qualification_type_repo.get_all_links(session=session)

    return all_links


@router.get(
    "/operation_to_qualification_type/{link_id}",
    response_model=OperationToQualificationTypeSchema,
    status_code=status.HTTP_200_OK,
)
async def get_operation_to_qualification_type_by_id(link_id: int) -> OperationToQualificationTypeSchema:
    try:
        async with database.session() as session:
            link = await operation_to_qualification_type_repo.get_link_by_id(session=session, link_id=link_id)
    except OperationToQualificationTypeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return link


@router.post(
    "/add_operation_to_qualification_type",
    response_model=OperationToQualificationTypeSchema,
    status_code=status.HTTP_201_CREATED,
)
async def add_operation_to_qualification_type(
        link_dto: OperationToQualificationTypeCreateUpdateSchema,
) -> OperationToQualificationTypeSchema:
    try:
        async with database.session() as session:
            new_link = await operation_to_qualification_type_repo.create_link(session=session, link=link_dto)
    except OperationToQualificationTypeAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_link


@router.put(
    "/update_operation_to_qualification_type/{link_id}",
    response_model=OperationToQualificationTypeSchema,
    status_code=status.HTTP_200_OK,
)
async def update_operation_to_qualification_type(
        link_id: int, link_dto: OperationToQualificationTypeCreateUpdateSchema
) -> OperationToQualificationTypeSchema:
    try:
        async with database.session() as session:
            updated_link = await operation_to_qualification_type_repo.update_link(
                session=session, link_id=link_id, link=link_dto
            )
    except OperationToQualificationTypeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_link


@router.delete(
    "/delete_operation_to_qualification_type/{link_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_operation_to_qualification_type(link_id: int) -> None:
    try:
        async with database.session() as session:
            await operation_to_qualification_type_repo.delete_link(session=session, link_id=link_id)
    except OperationToQualificationTypeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)


#
#
@router.get("/all_operations", response_model=list[OperationsSchema], status_code=status.HTTP_200_OK)
async def get_all_operations() -> list[OperationsSchema]:
    async with database.session() as session:
        all_operations = await operations_repo.get_all_operations(session=session)

    return all_operations


@router.get("/operation/{operation_id}", response_model=OperationsSchema, status_code=status.HTTP_200_OK)
async def get_operation_by_id(operation_id: int) -> OperationsSchema:
    try:
        async with database.session() as session:
            operation = await operations_repo.get_operation_by_id(session=session, operation_id=operation_id)
    except OperationNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return operation


@router.post("/add_operation", response_model=OperationsSchema, status_code=status.HTTP_201_CREATED)
async def add_operation(operation_dto: OperationsCreateUpdateSchema) -> OperationsSchema:
    try:
        async with database.session() as session:
            new_operation = await operations_repo.create_operation(session=session, operation=operation_dto)
    except OperationAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_operation


@router.put("/update_operation/{operation_id}", response_model=OperationsSchema, status_code=status.HTTP_200_OK)
async def update_operation(operation_id: int, operation_dto: OperationsCreateUpdateSchema) -> OperationsSchema:
    try:
        async with database.session() as session:
            updated_operation = await operations_repo.update_operation(
                session=session, operation_id=operation_id, operation=operation_dto
            )
    except OperationNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_operation


@router.delete("/delete_operation/{operation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_operation(operation_id: int) -> None:
    try:
        async with database.session() as session:
            await operations_repo.delete_operation(session=session, operation_id=operation_id)
    except OperationNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
#
#
#
@router.get("/all_operation_types", response_model=list[OperationTypesSchema], status_code=status.HTTP_200_OK)
async def get_all_operation_types() -> list[OperationTypesSchema]:
    async with database.session() as session:
        all_operation_types = await operation_types_repo.get_all_operation_types(session=session)

    return all_operation_types


@router.get("/operation_type/{operation_type_id}", response_model=OperationTypesSchema, status_code=status.HTTP_200_OK)
async def get_operation_type_by_id(operation_type_id: int) -> OperationTypesSchema:
    try:
        async with database.session() as session:
            operation_type = await operation_types_repo.get_operation_type_by_id(
                session=session, operation_type_id=operation_type_id
            )
    except OperationTypeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return operation_type


@router.post("/add_operation_type", response_model=OperationTypesSchema, status_code=status.HTTP_201_CREATED)
async def add_operation_type(operation_type_dto: OperationTypesCreateUpdateSchema) -> OperationTypesSchema:
    try:
        async with database.session() as session:
            new_operation_type = await operation_types_repo.create_operation_type(
                session=session, operation_type=operation_type_dto
            )
    except OperationTypeAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_operation_type


@router.put(
    "/update_operation_type/{operation_type_id}",
    response_model=OperationTypesSchema,
    status_code=status.HTTP_200_OK,
)
async def update_operation_type(
    operation_type_id: int, operation_type_dto: OperationTypesCreateUpdateSchema
) -> OperationTypesSchema:
    try:
        async with database.session() as session:
            updated_operation_type = await operation_types_repo.update_operation_type(
                session=session, operation_type_id=operation_type_id, operation_type=operation_type_dto
            )
    except OperationTypeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_operation_type


@router.delete("/delete_operation_type/{operation_type_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_operation_type(operation_type_id: int) -> None:
    try:
        async with database.session() as session:
            await operation_types_repo.delete_operation_type(session=session, operation_type_id=operation_type_id)
    except OperationTypeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

#
#
#
#
@router.get("/all_patients", response_model=list[PatientsSchema], status_code=status.HTTP_200_OK)
async def get_all_patients() -> list[PatientsSchema]:
    async with database.session() as session:
        all_patients = await patients_repo.get_all_patients(session=session)

    return all_patients


@router.get("/patient/{patient_id}", response_model=PatientsSchema, status_code=status.HTTP_200_OK)
async def get_patient_by_id(patient_id: int) -> PatientsSchema:
    try:
        async with database.session() as session:
            patient = await patients_repo.get_patient_by_id(session=session, patient_id=patient_id)
    except PatientNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return patient


@router.post("/add_patient", response_model=PatientsSchema, status_code=status.HTTP_201_CREATED)
async def add_patient(patient_dto: PatientsCreateUpdateSchema) -> PatientsSchema:
    try:
        async with database.session() as session:
            new_patient = await patients_repo.create_patient(session=session, patient=patient_dto)
    except PatientAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_patient


@router.put("/update_patient/{patient_id}", response_model=PatientsSchema, status_code=status.HTTP_200_OK)
async def update_patient(patient_id: int, patient_dto: PatientsCreateUpdateSchema) -> PatientsSchema:
    try:
        async with database.session() as session:
            updated_patient = await patients_repo.update_patient(
                session=session, patient_id=patient_id, patient=patient_dto
            )
    except PatientNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_patient


@router.delete("/delete_patient/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient(patient_id: int) -> None:
    try:
        async with database.session() as session:
            await patients_repo.delete_patient(session=session, patient_id=patient_id)
    except PatientNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

#
#
# # #
@router.get("/all_patient_receptions", response_model=list[PatientReceptionSchema], status_code=status.HTTP_200_OK)
async def get_all_patient_receptions() -> list[PatientReceptionSchema]:
    async with database.session() as session:
        all_receptions = await patient_reception_repo.get_all_patient_receptions(session=session)

    return all_receptions


@router.get("/patient_reception/{reception_id}", response_model=PatientReceptionSchema, status_code=status.HTTP_200_OK)
async def get_patient_reception_by_id(reception_id: int) -> PatientReceptionSchema:
    try:
        async with database.session() as session:
            reception = await patient_reception_repo.get_patient_reception_by_id(
                session=session, reception_id=reception_id
            )
    except PatientReceptionNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return reception


@router.post("/add_patient_reception", response_model=PatientReceptionSchema, status_code=status.HTTP_201_CREATED)
async def add_patient_reception(reception_dto: PatientReceptionCreateUpdateSchema) -> PatientReceptionSchema:
    try:
        async with database.session() as session:
            new_reception = await patient_reception_repo.create_patient_reception(
                session=session, reception=reception_dto
            )
    except PatientReceptionAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_reception


@router.put(
    "/update_patient_reception/{reception_id}",
    response_model=PatientReceptionSchema,
    status_code=status.HTTP_200_OK,
)
async def update_patient_reception(
    reception_id: int, reception_dto: PatientReceptionCreateUpdateSchema
) -> PatientReceptionSchema:
    try:
        async with database.session() as session:
            updated_reception = await patient_reception_repo.update_patient_reception(
                session=session, reception_id=reception_id, reception=reception_dto
            )
    except PatientReceptionNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_reception


@router.delete("/delete_patient_reception/{reception_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient_reception(reception_id: int) -> None:
    try:
        async with database.session() as session:
            await patient_reception_repo.delete_patient_reception(session=session, reception_id=reception_id)
    except PatientReceptionNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

#
#
#
@router.get("/all_positions", response_model=list[PositionSchema], status_code=status.HTTP_200_OK)
async def get_all_positions() -> list[PositionSchema]:
    async with database.session() as session:
        all_positions = await position_repo.get_all_positions(session=session)

    return all_positions


@router.get("/position/{position_id}", response_model=PositionSchema, status_code=status.HTTP_200_OK)
async def get_position_by_id(position_id: int) -> PositionSchema:
    try:
        async with database.session() as session:
            position = await position_repo.get_position_by_id(session=session, position_id=position_id)
    except PositionNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return position


@router.post("/add_position", response_model=PositionSchema, status_code=status.HTTP_201_CREATED)
async def add_position(position_dto: PositionCreateUpdateSchema) -> PositionSchema:
    try:
        async with database.session() as session:
            new_position = await position_repo.create_position(session=session, position=position_dto)
    except PositionAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_position


@router.put("/update_position/{position_id}", response_model=PositionSchema, status_code=status.HTTP_200_OK)
async def update_position(position_id: int, position_dto: PositionCreateUpdateSchema) -> PositionSchema:
    try:
        async with database.session() as session:
            updated_position = await position_repo.update_position(
                session=session, position_id=position_id, position=position_dto
            )
    except PositionNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_position


@router.delete("/delete_position/{position_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_position(position_id: int) -> None:
    try:
        async with database.session() as session:
            await position_repo.delete_position(session=session, position_id=position_id)
    except PositionNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
#
#
#
#
#
#
#
@router.get(
    "/all_qualification_doctors",
    response_model=list[QualificationDoctorSchema],
    status_code=status.HTTP_200_OK,
)
async def get_all_qualification_doctors() -> list[QualificationDoctorSchema]:
    async with database.session() as session:
        all_qualification_doctors = await qualification_doctor_repo.get_all_qualification_doctors(session=session)

    return all_qualification_doctors


@router.get(
    "/qualification_doctor/{qd_id}",
    response_model=QualificationDoctorSchema,
    status_code=status.HTTP_200_OK,
)
async def get_qualification_doctor_by_id(qd_id: int) -> QualificationDoctorSchema:
    try:
        async with database.session() as session:
            qualification_doctor = await qualification_doctor_repo.get_qualification_doctor_by_id(
                session=session, qd_id=qd_id
            )
    except QualificationDoctorNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return qualification_doctor


@router.post(
    "/add_qualification_doctor",
    response_model=QualificationDoctorSchema,
    status_code=status.HTTP_201_CREATED,
)
async def add_qualification_doctor(
    qd_dto: QualificationDoctorCreateUpdateSchema,
) -> QualificationDoctorSchema:
    try:
        async with database.session() as session:
            new_qualification_doctor = await qualification_doctor_repo.create_qualification_doctor(
                session=session, qd=qd_dto
            )
    except QualificationDoctorAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_qualification_doctor


@router.put(
    "/update_qualification_doctor/{qd_id}",
    response_model=QualificationDoctorSchema,
    status_code=status.HTTP_200_OK,
)
async def update_qualification_doctor(
    qd_id: int, qd_dto: QualificationDoctorCreateUpdateSchema
) -> QualificationDoctorSchema:
    try:
        async with database.session() as session:
            updated_qualification_doctor = await qualification_doctor_repo.update_qualification_doctor(
                session=session, qd_id=qd_id, qd=qd_dto
            )
    except QualificationDoctorNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_qualification_doctor


@router.delete("/delete_qualification_doctor/{qd_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qualification_doctor(qd_id: int) -> None:
    try:
        async with database.session() as session:
            await qualification_doctor_repo.delete_qualification_doctor(session=session, qd_id=qd_id)
    except QualificationDoctorNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

#
#
#
#
# @router.get(
#     "/all_qualification_types",
#     response_model=list[QualificationTypeSchema],
#     status_code=status.HTTP_200_OK,
# )
# async def get_all_qualification_types() -> list[QualificationTypeSchema]:
#     async with database.session() as session:
#         all_qualification_types = await qualification_type_repo.get_all_qualification_types(session=session)
#
#     return all_qualification_types
#
#
# @router.get(
#     "/qualification_type/{qt_id}",
#     response_model=QualificationTypeSchema,
#     status_code=status.HTTP_200_OK,
# )
# async def get_qualification_type_by_id(qt_id: int) -> QualificationTypeSchema:
#     try:
#         async with database.session() as session:
#             qualification_type = await qualification_type_repo.get_qualification_type_by_id(
#                 session=session, qt_id=qt_id
#             )
#     except QualificationTypeNotFound as error:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
#
#     return qualification_type
#
#
# @router.post(
#     "/add_qualification_type",
#     response_model=QualificationTypeSchema,
#     status_code=status.HTTP_201_CREATED,
# )
# async def add_qualification_type(
#     qt_dto: QualificationTypeCreateUpdateSchema,
# ) -> QualificationTypeSchema:
#     try:
#         async with database.session() as session:
#             new_qualification_type = await qualification_type_repo.create_qualification_type(
#                 session=session, qt=qt_dto
#             )
#     except QualificationTypeAlreadyExists as error:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)
#
#     return new_qualification_type
#
#
# @router.put(
#     "/update_qualification_type/{qt_id}",
#     response_model=QualificationTypeSchema,
#     status_code=status.HTTP_200_OK,
# )
# async def update_qualification_type(
#     qt_id: int, qt_dto: QualificationTypeCreateUpdateSchema
# ) -> QualificationTypeSchema:
#     try:
#         async with database.session() as session:
#             updated_qualification_type = await qualification_type_repo.update_qualification_type(
#                 session=session, qt_id=qt_id, qt=qt_dto
#             )
#     except QualificationTypeNotFound as error:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
#
#     return updated_qualification_type
#
#
# @router.delete("/delete_qualification_type/{qt_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_qualification_type(qt_id: int) -> None:
#     try:
#         async with database.session() as session:
#             await qualification_type_repo.delete_qualification_type(session=session, qt_id=qt_id)
#     except QualificationTypeNotFound as error:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
#
#
#
#

@router.get("/all_wards", response_model=list[WardSchema], status_code=status.HTTP_200_OK)
async def get_all_wards() -> list[WardSchema]:
    async with database.session() as session:
        all_wards = await ward_repo.get_all_wards(session=session)

    return all_wards


@router.get("/ward/{ward_id}", response_model=WardSchema, status_code=status.HTTP_200_OK)
async def get_ward_by_id(ward_id: int) -> WardSchema:
    try:
        async with database.session() as session:
            ward = await ward_repo.get_ward_by_id(session=session, ward_id=ward_id)
    except WardNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return ward


@router.post("/add_ward", response_model=WardSchema, status_code=status.HTTP_201_CREATED)
async def add_ward(ward_dto: WardCreateUpdateSchema) -> WardSchema:
    try:
        async with database.session() as session:
            new_ward = await ward_repo.create_ward(session=session, ward=ward_dto)
    except WardAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_ward


@router.put("/update_ward/{ward_id}", response_model=WardSchema, status_code=status.HTTP_200_OK)
async def update_ward(ward_id: int, ward_dto: WardCreateUpdateSchema) -> WardSchema:
    try:
        async with database.session() as session:
            updated_ward = await ward_repo.update_ward(session=session, ward_id=ward_id, ward=ward_dto)
    except WardNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_ward


@router.delete("/delete_ward/{ward_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ward(ward_id: int) -> None:
    try:
        async with database.session() as session:
            await ward_repo.delete_ward(session=session, ward_id=ward_id)
    except WardNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
