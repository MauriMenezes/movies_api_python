from pydantic import BaseModel
from typing import Optional


class Movie(BaseModel):
    title: str
    year: int
    detailes: Optional[str] = None
