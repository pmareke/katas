from doublex import Mimic, Mock
from doublex_expects import have_been_satisfied
from expects import expect
from typing import List


from bank.src.domain.transaction import Transaction, TransactionType
from bank.src.domain.amount import Amount
from bank.src.infrastructure.console_output import Console
from bank.src.infrastructure.statement_printer import StatementPrinter


def deposit(day: str, amount: Amount) -> Transaction:
    return Transaction(TransactionType.DEPOSIT, day, amount)


def withdraw(day: str, amount: Amount) -> Transaction:
    return Transaction(TransactionType.WITHDRAW, day, amount)


class TestStatementPrinter:
    def test_prints_the_header(self) -> None:
        with Mimic(Mock, Console) as console:
            console.print_line("date || credit || debit || balance")
        statement_printer = StatementPrinter(console)
        transactions: List[Transaction] = []

        statement_printer.print(transactions)

        expect(console).to(have_been_satisfied)

    def test_prints_one_deposit_transaction(self) -> None:
        with Mimic(Mock, Console) as console:
            console.print_line("date || credit || debit || balance")
            console.print_line("12/01/2012 || 1000.00 || || 1000.00")
        statement_printer = StatementPrinter(console)
        transactions = [deposit("12/01/2012", Amount(1000))]

        statement_printer.print(transactions)

        expect(console).to(have_been_satisfied)

    def test_prints_one_withdraw_transaction(self) -> None:
        with Mimic(Mock, Console) as console:
            console.print_line("date || credit || debit || balance")
            console.print_line("12/01/2012 || || 1000.00 || -1000.00")
        statement_printer = StatementPrinter(console)
        transactions = [withdraw("12/01/2012", Amount(1000))]

        statement_printer.print(transactions)

        expect(console).to(have_been_satisfied)

    def test_prints_transactions_in_chronological_order(self) -> None:
        with Mimic(Mock, Console) as console:
            console.print_line("date || credit || debit || balance")
            console.print_line("14/01/2012 || 500.00 || || 1400.00")
            console.print_line("13/01/2012 || || 100.00 || 900.00")
            console.print_line("12/01/2012 || 1000.00 || || 1000.00")
        statement_printer = StatementPrinter(console)
        transactions = [
            deposit("12/01/2012", Amount(1000)),
            withdraw("13/01/2012", Amount(100)),
            deposit("14/01/2012", Amount(500)),
        ]

        statement_printer.print(transactions)

        expect(console).to(have_been_satisfied)
