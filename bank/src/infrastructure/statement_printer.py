from typing import List

from bank.src.domain.transaction import Transaction, TransactionType
from bank.src.infrastructure.interfaces.output import Output
from bank.src.infrastructure.interfaces.printer import Printer


class StatementPrinter(Printer):
    def __init__(self, console: Output) -> None:
        self.console = console

    def print(self, transactions: List[Transaction]) -> None:
        total = 0
        self.console.print_line("date || credit || debit || balance")
        lines: List[str] = []
        for transaction in transactions:
            if transaction.type == TransactionType.DEPOSIT:
                total += transaction.amount
                lines.append(
                    f"{transaction.day} || {transaction.amount:.2f} || || {total:.2f}"
                )
            if transaction.type == TransactionType.WITHDRAW:
                total -= transaction.amount
                lines.append(
                    f"{transaction.day} || || {transaction.amount:.2f} || {total:.2f}"
                )

        [self.console.print_line(line) for line in reversed(lines)]
