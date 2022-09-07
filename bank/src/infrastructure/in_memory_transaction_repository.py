from typing import List

from bank.src.domain.clock import Clock
from bank.src.domain.transaction_repository import TransactionRepository
from bank.src.domain.transaction import Transaction, TransactionType


class InMemoryTransactionTransactionRepository(TransactionRepository):
    def __init__(self, clock: Clock) -> None:
        self.clock = clock
        self.transactions: List[Transaction] = []

    def add_deposit(self, deposit: int) -> None:
        self.transactions.append(
            Transaction(TransactionType.DEPOSIT, self.clock.today(), deposit)
        )

    def add_withdraw(self, withdraw: int) -> None:
        self.transactions.append(
            Transaction(TransactionType.WITHDRAW, self.clock.today(), withdraw)
        )

    def all_transactions(self) -> List[Transaction]:
        return self.transactions
