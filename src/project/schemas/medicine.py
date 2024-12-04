from pydantic import ConfigDict, BaseModel


class MedicineCreateUpdateSchema(BaseModel):
    name: str
    description: str


class MedicineSchema(MedicineCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
