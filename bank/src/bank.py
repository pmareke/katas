from bank.src.account_service import AccountService
from bank.src.transaction_repository import TransactionRepository
from bank.src.statement_printer import StatementPrinter


class Account(AccountService):
    def __init__(
        self,
        transaction_repository: TransactionRepository,
        statement_printer: StatementPrinter,
    ) -> None:
        self.transition_repository = transaction_repository
        self.statement_printer = statement_printer

    def deposit(self, amount: int) -> None:
        self.transition_repository.add_deposit(amount)

    def withdraw(self, amount: int) -> None:
        self.transition_repository.add_withdraw(amount)

    def print_statement(self) -> None:
        transactions = self.transition_repository.all_transactions()
        self.statement_printer.print(transactions)
