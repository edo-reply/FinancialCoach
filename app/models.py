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

        if type(self.category) is str:
            self.category = TRANSACTION_CATEGORIES.index(self.category.lower())


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


TRANSACTION_CATEGORIES = [
    'transportation / extra transport',                 # o
    'rent & utilities',                                 # 1
    'medical',                                          # 2
    'transportation / gas',                             # 3
    'travel',                                           # 4
    'transportation / parking',                         # 5
    'transportation / automobile maintenance and fees', # 6
    'loans',                                            # 7
    'general services',                                 # 8
    'government + non-profit / taxes',                  # 9
    'income / other',                                   # 10
    'income / wages, gig economy, tips',                # 11
    'charity & donations',                              # 12
    'general merchandise',                              # 13
    'food & drink / restaurants',                       # 14
    'food & drink / other',                             # 15
    'food & drink / groceries',                         # 16
    'entertainment / services',                         # 17
    'food & drink / alcohol & bars',                    # 18
    'bank transfers / savings',                         # 19
    'bank transfers / transfers',                       # 20
    'bank transfers / fees',                            # 21
    'entertainment / activities'                        # 22
]

def update_model(dst, src):
    if not is_dataclass(src) or not is_dataclass(dst):
        raise NotImplementedError
    
    for field in fields(src):
        value = getattr(src, field.name)
        if value is not None:
            setattr(dst, field.name, value)
