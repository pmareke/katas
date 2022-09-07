from bank.src.domain.account_service import AccountService
from bank.src.domain.printer import Printer
from bank.src.domain.repository import Repository


class Account(AccountService):
    def __init__(
        self,
        transaction_repository: Repository,
        statement_printer: Printer,
    ) -> None:
        self.transition_repository = transaction_repository
        self.statement_printer = statement_printer

    def deposit(self, amount: int) -> None:
        self.transition_repository.add_deposit(amount)

    def withdraw(self, amount: int) -> None:
        self.transition_repository.add_withdraw(amount)

    def print_statement(self) -> None:
        self.statement_printer.print(self.transition_repository.all_transactions())
