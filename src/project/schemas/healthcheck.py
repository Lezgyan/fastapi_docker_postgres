from pydantic import BaseModel

# проверяем жива ли база
class HealthCheckSchema(BaseModel):
    db_is_ok: bool
