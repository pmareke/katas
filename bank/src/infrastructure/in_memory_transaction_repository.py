from typing import List

from bank.src.domain.amount import Amount
from bank.src.domain.transaction import Transaction, TransactionType
from bank.src.domain.transaction_repository import TransactionRepository
from bank.src.infrastructure.interfaces.clock import Clock


class InMemoryTransactionRepository(TransactionRepository):

    def __init__(self, clock: Clock) -> None:
        self.clock = clock
        self.transactions: List[Transaction] = []

    def add_deposit(self, deposit: Amount) -> None:
        self.transactions.append(
            Transaction(TransactionType.DEPOSIT, self.clock.today(), deposit))

    def add_withdraw(self, withdraw: Amount) -> None:
        self.transactions.append(
            Transaction(TransactionType.WITHDRAW, self.clock.today(),
                        withdraw))

    def all_transactions(self) -> List[Transaction]:
        return self.transactions
