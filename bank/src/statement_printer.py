from typing import List

from bank.src.transaction import Transaction, TransactionType
from bank.src.console import Console


class StatementPrinter:
    def __init__(self, console: Console) -> None:
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

        for line in reversed(lines):
            self.console.print_line(line)
