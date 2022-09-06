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


class Account(AccountService):
    def __init__(self) -> None:
        pass

    def deposit(self, amount: int, date: str) -> None:
        pass

    def withdraw(self, amount: int, date: str) -> None:
        pass

    def print_statement(self) -> str:
        return ""
