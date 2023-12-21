from dataclasses import dataclass, is_dataclass, fields
from datetime import datetime
from typing import Any, Mapping


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

def get_fields(obj) -> Mapping[str, Any]:
    if not is_dataclass(obj):
        return {}
    return {
        field.name: getattr(obj, field.name)
        for field in fields(obj)
        if getattr(obj, field.name) is not None
    }
