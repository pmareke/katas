from doublex import Mimic, Mock
from doublex_expects import have_been_satisfied
from expects import expect

from bank.src.domain.transaction import Transaction, TransactionType
from bank.src.infrastructure.console_output import Console
from bank.src.infrastructure.statement_printer import StatementPrinter


def deposit(day: str, amount: int) -> Transaction:
    return Transaction(TransactionType.DEPOSIT, day, amount)


def withdraw(day: str, amount: int) -> Transaction:
    return Transaction(TransactionType.WITHDRAW, day, amount)


class TestStatementPrinter:
    def test_prints_the_header(self) -> None:
        with Mimic(Mock, Console) as console:
            console.print_line("date || credit || debit || balance")

        statement_printer = StatementPrinter(console)

        statement_printer.print([])

        expect(console).to(have_been_satisfied)

    def test_prints_one_deposit_transaction(self) -> None:
        with Mimic(Mock, Console) as console:
            console.print_line("date || credit || debit || balance")
            console.print_line("12/01/2012 || 1000.00 || || 1000.00")

        statement_printer = StatementPrinter(console)

        statement_printer.print([deposit("12/01/2012", 1000)])

        expect(console).to(have_been_satisfied)

    def test_prints_one_withdraw_transaction(self) -> None:
        with Mimic(Mock, Console) as console:
            console.print_line("date || credit || debit || balance")
            console.print_line("12/01/2012 || || 1000.00 || -1000.00")

        statement_printer = StatementPrinter(console)

        statement_printer.print([withdraw("12/01/2012", 1000)])

        expect(console).to(have_been_satisfied)

    def test_prints_transactions_in_chronological_order(self) -> None:
        with Mimic(Mock, Console) as console:
            console.print_line("date || credit || debit || balance")
            console.print_line("14/01/2012 || 500.00 || || 1400.00")
            console.print_line("13/01/2012 || || 100.00 || 900.00")
            console.print_line("12/01/2012 || 1000.00 || || 1000.00")
        statement_printer = StatementPrinter(console)

        statement_printer.print(
            [
                deposit("12/01/2012", 1000),
                withdraw("13/01/2012", 100),
                deposit("14/01/2012", 500),
            ]
        )

        expect(console).to(have_been_satisfied)
