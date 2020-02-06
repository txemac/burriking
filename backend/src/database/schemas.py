from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class BaristaPost(BaseModel):
    username: str = Field(..., min_length=3, max_length=150)


class BaristaGet(BaristaPost):
    id: int = Field(..., gt=0)
    dt_created: datetime

    class Config:
        orm_mode = True
