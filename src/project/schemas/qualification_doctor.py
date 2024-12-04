from pydantic import ConfigDict, BaseModel


class QualificationDoctorCreateUpdateSchema(BaseModel):
    doctor_id: int
    qualification_id: int


class QualificationDoctorSchema(QualificationDoctorCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
