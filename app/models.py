from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: str
    first_name: str
    last_name: str
    budget: float  # TODO change to appropriate currency type


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
