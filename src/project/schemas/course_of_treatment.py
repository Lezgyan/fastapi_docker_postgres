from datetime import datetime

from pydantic import ConfigDict, BaseModel


class CourseOfTreatmentCreateUpdateSchema(BaseModel):
    history_id: int
    description: str
    receipt_date: datetime
    doctor_id: int


class CourseOfTreatmentSchema(CourseOfTreatmentCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
