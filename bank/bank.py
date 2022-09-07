from bank.account_service import AccountService
from typing import List


class Account(AccountService):
    def __init__(self) -> None:
        self.total = 0
        self.movements: List[str] = []

    def deposit(self, amount: int) -> None:
        pass

    def withdraw(self, amount: int) -> None:
        pass

    def print_statement(self) -> None:
        pass
