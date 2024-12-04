from pydantic import BaseModel, ConfigDict


class DepartmentsCreateUpdateSchema(BaseModel):
    name: str


class DepartmentsSchema(DepartmentsCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    department_id: int
