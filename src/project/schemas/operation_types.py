from pydantic import ConfigDict, BaseModel


class OperationTypesCreateUpdateSchema(BaseModel):
    name: str


class OperationTypesSchema(OperationTypesCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    operation_type_id: int
