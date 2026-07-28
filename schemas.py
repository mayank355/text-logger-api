from pydantic import BaseModel
from typing import Optional

class TextCreate(BaseModel):
    content: str
    author: Optional[str] = "anonymous"

class TextResponse(BaseModel):
    id: int
    content: str
    author: str
    word_count: int

    class Config:
        from_attributes = True