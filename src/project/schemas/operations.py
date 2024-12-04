from datetime import datetime

from pydantic import ConfigDict, Field, BaseModel


class OperationsCreateUpdateSchema(BaseModel):
    history_id: int
    doctor_id: int
    operation_type_id: int
    operation_date: datetime
    description: str | None = Field(default=None)


class OperationsSchema(OperationsCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    operation_id: int
