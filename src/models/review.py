from pydantic import BaseModel


class ReviewIn(BaseModel):
    text: str


class ReviewOut(ReviewIn):
    id: int
    text: str
    sentiment: str
    created_at: str
