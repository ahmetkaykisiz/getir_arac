from datetime import date

from pydantic import BaseModel, Field
from typing import Optional, List, Any


class DriverRequest(BaseModel):
    maxScore: float = None
    minScore: float = None
    startDate: date = None
    endDate: date = None
    limit: int = Field(default=20, ge=1, le=150)
    offset: int = 0


class Driver(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    age: int
    driving_score: float
    created_at: date = None
    updated_at: date = None


class DriverPydantic(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    age: int
    driving_score: float
    created_at: date = None
    updated_at: date = None

    class Config:
        orm_mode = True
        from_attributes = True


class PageModel(BaseModel):
    page: int
    size: int
    items: List[Any]
    previous_page: Optional[int] = None
    next_page: Optional[int] = None
    has_previous: bool
    has_next: bool
    total: int

    class Config:
        orm_mode = True
        from_attributes = True

    @classmethod
    def from_orm_with_pagination(cls, page, size, items, total):
        pages = max(1, (total - 1) // size + 1)
        has_previous = page > 0
        has_next = (page + 1) * size < total
        previous_page = page - 1 if has_previous else None
        next_page = page + 1 if has_next else None

        return cls(
            page=page,
            size=size,
            items=items,
            previous_page=previous_page,
            next_page=next_page,
            has_previous=has_previous,
            has_next=has_next,
            total=total
        )
