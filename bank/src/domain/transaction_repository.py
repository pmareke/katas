from abc import ABC, abstractmethod

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
    def all_transactions(self) -> list[Transaction]:
        raise NotImplementedError
