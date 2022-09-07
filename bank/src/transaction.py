from dataclasses import dataclass
from enum import Enum


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


@dataclass
class Transaction:
    type: TransactionType
    day: str
    amount: int
