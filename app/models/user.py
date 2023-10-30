from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class User:
    id: UUID
    first_name: str
    last_name: str

    def to_dict(self) -> dict:
        _dict = self.__dict__.copy()
        _dict["id"] = str(self.id)
        return _dict
