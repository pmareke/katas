from abc import abstractmethod, ABC
from typing import List

from bank.src.domain.transaction import Transaction


class Printer(ABC):
    @abstractmethod
    def print(self, transactions: List[Transaction]) -> None:
        raise NotImplementedError
