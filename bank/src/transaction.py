from dataclasses import dataclass
from enum import auto, Enum


class TransactionType(Enum):
    DEPOSIT = auto()
    WITHDRAW = auto()


@dataclass
class Transaction:
    type: TransactionType
    day: str
    amount: int
