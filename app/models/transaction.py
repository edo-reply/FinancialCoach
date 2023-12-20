from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    id: str
    user_id: str
    description: str
    amount: float  # TODO change to appropriate currency type
    category: int
    recurring_event: bool
    created_on: datetime = datetime.now()
    rating: int = -1

    def __post_init__(self):
        pass

    def to_dict(self) -> dict:
        _dict = self.__dict__.copy()
        _dict["id"] = str(self.id)
        _dict["user_id"] = str(self.user_id)
        return _dict
