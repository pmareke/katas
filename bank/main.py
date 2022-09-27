from bank.src.infrastructure.console_output import Console
from bank.src.infrastructure.datetime_clock import DatetimeClock
from bank.src.infrastructure.in_memory_transaction_repository import (
    InMemoryTransactionRepository, )
from bank.src.infrastructure.statement_printer import StatementPrinter
from bank.src.uses_cases.account import Account
from bank.src.domain.amount import Amount


def main() -> None:
    clock = DatetimeClock()
    transaction_repository = InMemoryTransactionRepository(clock)
    console = Console()
    statement_printer = StatementPrinter(console)
    account = Account(transaction_repository, statement_printer)

    account.deposit(Amount(1000))
    account.withdraw(Amount(100))
    account.deposit(Amount(2000))

    account.print_statement()


if __name__ == "__main__":
    main()
