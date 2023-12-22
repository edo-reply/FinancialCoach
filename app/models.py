from dataclasses import dataclass, is_dataclass, fields
from datetime import datetime
from enum import Enum


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
    rating: float | None = None

    def __post__init__(self):
        # Throw exception if it is not a valid rating
        RatingClass.of(self.rating)


class RatingClass(Enum):
    Need = 3
    Love = 2
    Want = 1
    Like = 0
    Unknown = -1

    def eq(self, rating: float | None):
        return self == RatingClass.of(rating)

    @staticmethod
    def of(rating: float | None):
        if rating == None:
            return RatingClass.Unknown
        else:
            return RatingClass(int(rating))


def update_model(dst, src):
    if not is_dataclass(src) or not is_dataclass(dst):
        raise NotImplementedError
    
    for field in fields(src):
        value = getattr(src, field.name)
        if value is not None:
            setattr(dst, field.name, value)
