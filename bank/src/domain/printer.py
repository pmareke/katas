from abc import ABC
from typing import List

from bank.src.domain.transaction import Transaction


class Printer(ABC):
    def print(self, transactions: List[Transaction]) -> None:
        raise NotImplementedError
