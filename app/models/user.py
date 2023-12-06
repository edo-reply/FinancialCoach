from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    id: UUID
    first_name: str
    last_name: str
    budget: float  # TODO change to appropriate currency type

    def __post_init__(self):
        if type(self.budget) is not float:
            raise TypeError

    def to_dict(self) -> dict:
        _dict = self.__dict__.copy()
        _dict["id"] = str(self.id)
        return _dict
