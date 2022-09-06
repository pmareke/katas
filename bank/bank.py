from bank.account_service import AccountService


class Account(AccountService):
    def __init__(self) -> None:
        pass

    def deposit(self, amount: int, date: str) -> None:
        pass

    def withdraw(self, amount: int, date: str) -> None:
        pass

    def print_statement(self) -> str:
        return ""
