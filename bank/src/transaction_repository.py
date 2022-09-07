from typing import List
from bank.src.transaction import Transaction, TransactionType
from bank.src.clock import Clock


class TransactionRepository:
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
