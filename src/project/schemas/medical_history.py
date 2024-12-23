from datetime import datetime

from pydantic import ConfigDict, Field, BaseModel


class MedicalHistoryCreateUpdateSchema(BaseModel):
    patient_id: int
    disease_id: int
    doctor_id: int
    admission_date: datetime
    discharge_date: datetime | None = Field(default=None)
    notes: str | None = Field(default=None)
    ward_id: int


class MedicalHistorySchema(MedicalHistoryCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    history_id: int
