from typing import List, Tuple

from bank.src.domain.printer import Printer
from bank.src.domain.transaction import Transaction, TransactionType
from bank.src.infrastructure.interfaces.output import Output


class StatementPrinter(Printer):
    def __init__(self, console: Output) -> None:
        self.console = console

    def print(self, transactions: List[Transaction]) -> None:
        self.console.print_line("date || credit || debit || balance")
        self._print_lines(transactions)

    def _print_lines(self, transactions: List[Transaction]) -> None:
        statement_lines = self._statement_lines(transactions)
        for line in reversed(statement_lines):
            self.console.print_line(line)

    def _statement_lines(self, transactions: List[Transaction]) -> List[str]:
        balance = 0
        statement_lines: List[str] = []
        for transaction in transactions:
            line, balance = self.statement_line(transaction, balance)
            statement_lines.append(line)
        return statement_lines

    def statement_line(self, transaction: Transaction, balance: int) -> Tuple:
        line = None

        if transaction.type == TransactionType.DEPOSIT:
            balance += transaction.amount
            line = f"{transaction.day} || {transaction.amount:.2f} || || {balance:.2f}"
        elif transaction.type == TransactionType.WITHDRAW:
            balance -= transaction.amount
            line = f"{transaction.day} || || {transaction.amount:.2f} || {balance:.2f}"

        return (line, balance)
