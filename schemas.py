from datetime import datetime
from typing import Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, field_validator


class AlertCreate(BaseModel):
    title: str
    severity: Literal["critical", "warning", "info"]
    source: str
    metric_name: str
    metric_value: float
    threshold: float


class AlertOut(AlertCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: AwareDatetime

    @field_validator("created_at", mode="before")
    @classmethod
    def restore_utc(cls, value: datetime) -> datetime:
        from datetime import timezone

        if isinstance(value, datetime) and value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value


class ExplainResponse(BaseModel):
    alert_id: int
    explanation: str
    generated_at: AwareDatetime