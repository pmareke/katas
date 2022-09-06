from abc import ABC, abstractmethod


class AccountService(ABC):
    @abstractmethod
    def deposit(self, amount: int, date: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def withdraw(self, amount: int, date: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def print_statement(self) -> str:
        raise NotImplementedError
