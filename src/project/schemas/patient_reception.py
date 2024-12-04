from datetime import datetime

from pydantic import ConfigDict, BaseModel


class PatientReceptionCreateUpdateSchema(BaseModel):
    date: datetime
    description: str
    course_of_treatment_id: int
    medication_id: int


class PatientReceptionSchema(PatientReceptionCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
