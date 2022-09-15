from dataclasses import dataclass
from enum import auto, Enum

from bank.src.domain.amount import Amount


class TransactionType(Enum):
    DEPOSIT = auto()
    WITHDRAW = auto()


@dataclass
class Transaction:
    type: TransactionType
    day: str
    amount: Amount
