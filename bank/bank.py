from bank.account_service import AccountService
from typing import List


class Account(AccountService):
    def __init__(self) -> None:
        self.total = 0
        self.movements: List[str] = []

    def deposit(self, amount: int, date: str) -> None:
        self.total += amount
        self.movements.append(
            f"{date} || {amount:.2f}  ||          || {self.total:.2f}"
        )

    def withdraw(self, amount: int, date: str) -> None:
        self.total -= amount
        self.movements.append(
            f"{date} ||          || {amount:.2f}   || {self.total:.2f}"
        )

    def print_statement(self) -> str:
        header = "date       || credit   || debit    || balance"
        return "\n".join([header, *reversed(self.movements)])
