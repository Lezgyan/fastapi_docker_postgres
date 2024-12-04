from pydantic import BaseModel, ConfigDict, Field


class DiseasesCreateUpdateSchema(BaseModel):
    name: str
    icd_code: str
    description: str | None = Field(default=None)


class DiseasesSchema(DiseasesCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    disease_id: int
