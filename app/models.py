from dataclasses import dataclass, is_dataclass, fields
from datetime import datetime


@dataclass
class User:
    id: str
    first_name: str | None = None
    last_name: str | None = None
    budget: float | None = None


@dataclass
class Transaction:
    id: str
    user_id: str
    description: str | None = None
    amount: float | None = None
    category: int | None = None
    recurring_event: bool | None = None
    created_on: datetime | None = None
    rating: int | None = None


def update_model(dst, src):
    if not is_dataclass(src) or not is_dataclass(dst):
        raise NotImplementedError
    
    for field in fields(src):
        value = getattr(src, field.name)
        if value is not None:
            setattr(dst, field.name, value)
