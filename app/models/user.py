from dataclasses import dataclass


@dataclass
class User:
    id: str
    first_name: str
    last_name: str
    budget: float  # TODO change to appropriate currency type

    def __post_init__(self):
        pass

    def to_dict(self) -> dict:
        _dict = self.__dict__.copy()
        _dict["id"] = str(self.id)
        return _dict
