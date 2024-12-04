from pydantic import BaseModel, ConfigDict

class WardCreateUpdateSchema(BaseModel):
    name: str
    count_bunk: int
    department_id: int

class WardSchema(WardCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
