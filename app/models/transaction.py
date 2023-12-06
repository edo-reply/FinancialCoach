from dataclasses import dataclass
from uuid import UUID


@dataclass
class UserTransaction:
    id: UUID
    user_id: UUID
    details: str
    amount: float  # TODO change to appropriate currency type
    category: int
    recurring_event: bool
    rating: int = -1

    def __post_init__(self):
        if type(self.amount) is not float:
            raise TypeError(f"type(amount)={type(self.amount)} but should be float")
        if type(self.category) is not int:
            raise TypeError(f"type(category)={type(self.category)} but should be int")
        if type(self.recurring_event) is not bool:
            self.recurring_event = self.recurring_event.lower() in ['true', 't', '1', 'y', 'yes']
        if type(self.rating) is not int:
            raise TypeError(f"type(rating)={type(self.rating)} but should be int")

    def to_dict(self) -> dict:
        _dict = self.__dict__.copy()
        _dict["id"] = str(self.id)
        _dict["user_id"] = str(self.user_id)
        return _dict
