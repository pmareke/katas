from abc import ABC, abstractmethod


class AccountService(ABC):
    @abstractmethod
    def deposit(self, amount: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def withdraw(self, amount: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def print_statement(self) -> None:
        raise NotImplementedError
