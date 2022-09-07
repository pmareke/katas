from abc import ABC, abstractmethod
from typing import List

from bank.src.domain.transaction import Transaction


class Repository(ABC):
    @abstractmethod
    def add_deposit(self, deposit: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_withdraw(self, withdraw: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def all_transactions(self) -> List[Transaction]:
        raise NotImplementedError
