from pydantic import ConfigDict, BaseModel


class PatientsCreateUpdateSchema(BaseModel):
    full_name: str
    date_of_birth: str
    snils: str
    medical_policy: str


class PatientsSchema(PatientsCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    patient_id: int
