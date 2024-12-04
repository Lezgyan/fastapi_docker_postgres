from pydantic import ConfigDict, BaseModel


class OperationToQualificationTypeCreateUpdateSchema(BaseModel):
    operation_type_id: int
    qualification_type_id: int


class OperationToQualificationTypeSchema(OperationToQualificationTypeCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
