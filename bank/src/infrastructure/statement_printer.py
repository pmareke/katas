from typing import List, Tuple

from bank.src.domain.transaction import Transaction, TransactionType
from bank.src.infrastructure.interfaces.output import Output
from bank.src.infrastructure.interfaces.printer import Printer


class StatementPrinter(Printer):
    def __init__(self, console: Output) -> None:
        self.console = console

    def print(self, transactions: List[Transaction]) -> None:
        self.console.print_line("date || credit || debit || balance")
        total = 0
        lines: List[str] = []
        for transaction in transactions:
            line, total = self.transaction_line(transaction, total)
            lines.append(line)

        [self.console.print_line(line) for line in reversed(lines)]

    def transaction_line(self, transaction: Transaction, total: int) -> Tuple:
        line = None

        if transaction.type == TransactionType.DEPOSIT:
            total += transaction.amount
            line = f"{transaction.day} || {transaction.amount:.2f} || || {total:.2f}"
        elif transaction.type == TransactionType.WITHDRAW:
            total -= transaction.amount
            line = f"{transaction.day} || || {transaction.amount:.2f} || {total:.2f}"

        return (line, total)
