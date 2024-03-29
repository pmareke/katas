from doublex import Mimic, Stub
from expects import be, expect, equal

from bank.src.domain.transaction import Transaction, TransactionType
from bank.src.domain.amount import Amount
from bank.src.infrastructure.datetime_clock import DatetimeClock
from bank.src.infrastructure.in_memory_transaction_repository import (
    InMemoryTransactionRepository, )


class TestTransactionRepository:

    def test_adds_a_deposit_transaction(self) -> None:
        day = "12/01/2012"
        deposit = Amount(1000)
        with Mimic(Stub, DatetimeClock) as clock:
            clock.today().returns(day)
        transaction_repository = InMemoryTransactionRepository(clock)

        transaction_repository.add_deposit(deposit)
        transactions = transaction_repository.all_transactions()

        expect(len(transactions)).to(be(1))
        expect(transactions[0]).to(
            equal(Transaction(TransactionType.DEPOSIT, day, deposit)))

    def test_adds_a_withdraw_transaction(self) -> None:
        day = "12/01/2012"
        withdraw = Amount(1000)
        with Mimic(Stub, DatetimeClock) as clock:
            clock.today().returns(day)
        transaction_repository = InMemoryTransactionRepository(clock)

        transaction_repository.add_withdraw(withdraw)
        transactions = transaction_repository.all_transactions()

        expect(len(transactions)).to(be(1))
        expect(transactions[0]).to(
            equal(Transaction(TransactionType.WITHDRAW, day, withdraw)))
