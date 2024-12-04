from pydantic import BaseModel, ConfigDict


class PositionCreateUpdateSchema(BaseModel):
    name: str


class PositionSchema(PositionCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    position_id: int
