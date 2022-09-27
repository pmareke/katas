from abc import ABC, abstractmethod
from bank.src.domain.amount import Amount


class AccountService(ABC):

    @abstractmethod
    def deposit(self, amount: Amount) -> None:
        raise NotImplementedError

    @abstractmethod
    def withdraw(self, amount: Amount) -> None:
        raise NotImplementedError

    @abstractmethod
    def print_statement(self) -> None:
        raise NotImplementedError
