from pydantic import BaseModel


class ProgressDto(BaseModel):
    nowValue: int
    maxValue: int
