from pydantic import ConfigDict, BaseModel


class DoctorsCreateUpdateSchema(BaseModel):
    full_name: str
    position_id: int
    department_id: int


class DoctorsSchema(DoctorsCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    doctor_id: int
