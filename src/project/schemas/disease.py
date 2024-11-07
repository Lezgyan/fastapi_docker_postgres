from pydantic import BaseModel, Field, ConfigDict


class DiseaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    disease_id: int
    name: str
    icd_code: str
    description: str

print(DiseaseSchema(disease_id=1, name="Сопли", icd_code="123", description="bad").dict())