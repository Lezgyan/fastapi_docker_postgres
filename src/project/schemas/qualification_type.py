from pydantic import ConfigDict, BaseModel


class QualificationTypeCreateUpdateSchema(BaseModel):
    name: str


class QualificationTypeSchema(QualificationTypeCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
