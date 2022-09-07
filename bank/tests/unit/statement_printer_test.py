from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect

from bank.src.console import Console
from bank.src.statement_printer import StatementPrinter
from bank.src.transaction import Transaction, TransactionType


class TestStatementPrinter:
    def test_prints_the_header(self) -> None:
        console = Mimic(Spy, Console)
        statement_printer = StatementPrinter(console)

        statement_printer.print([])

        expect(console.print_line).to(
            have_been_called_with("date || credit || debit || balance")
        )

    def test_prints_one_deposit_transaction(self) -> None:
        console = Mimic(Spy, Console)
        statement_printer = StatementPrinter(console)

        statement_printer.print(
            [Transaction(TransactionType.DEPOSIT, "12/01/2012", 1000)]
        )

        expect(console.print_line).to(
            have_been_called_with("date || credit || debit || balance")
        )
        expect(console.print_line).to(
            have_been_called_with("12/01/2012 || 1000.00 || || 1000.00")
        )

    def test_prints_one_withdraw_transaction(self) -> None:
        console = Mimic(Spy, Console)
        statement_printer = StatementPrinter(console)

        statement_printer.print(
            [Transaction(TransactionType.WITHDRAW, "12/01/2012", 1000)]
        )

        expect(console.print_line).to(
            have_been_called_with("date || credit || debit || balance")
        )
        expect(console.print_line).to(
            have_been_called_with("12/01/2012 || || 1000.00 || -1000.00")
        )

    def test_prints_transactions_in_chronological_order(self) -> None:
        console = Mimic(Spy, Console)
        statement_printer = StatementPrinter(console)

        statement_printer.print(
            [
                Transaction(TransactionType.DEPOSIT, "12/01/2012", 1000),
                Transaction(TransactionType.WITHDRAW, "13/01/2012", 100),
                Transaction(TransactionType.DEPOSIT, "14/01/2012", 500),
            ]
        )

        expect(console.print_line).to(
            have_been_called_with("date || credit || debit || balance")
        )
        expect(console.print_line).to(
            have_been_called_with("14/01/2012 || 500.00 || || 1400.00")
        )
        expect(console.print_line).to(
            have_been_called_with("13/01/2012 || || 100.00 || 900.00")
        )
        expect(console.print_line).to(
            have_been_called_with("12/01/2012 || 1000.00 || || 1000.00")
        )
