from abc import ABC, abstractmethod
from typing import List

from bank.src.domain.amount import Amount
from bank.src.domain.transaction import Transaction


class TransactionRepository(ABC):

    @abstractmethod
    def add_deposit(self, deposit: Amount) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_withdraw(self, withdraw: Amount) -> None:
        raise NotImplementedError

    @abstractmethod
    def all_transactions(self) -> List[Transaction]:
        raise NotImplementedError
