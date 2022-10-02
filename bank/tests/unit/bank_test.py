from typing import List

from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect

from bank.src.uses_cases.account import Account
from bank.src.domain.amount import Amount
from bank.src.domain.transaction import Transaction, TransactionType
from bank.src.infrastructure.in_memory_transaction_repository import (
    InMemoryTransactionRepository,
)
from bank.src.infrastructure.statement_printer import StatementPrinter


class TestBank:
    def test_stores_a_deposit_transaction(self) -> None:
        deposit = Amount(1000)
        transaction_repository = Mimic(Spy, InMemoryTransactionRepository)
        statement_printer = Mimic(Spy, StatementPrinter)
        account = Account(transaction_repository, statement_printer)

        account.deposit(deposit)

        expect(transaction_repository.add_deposit).to(
            have_been_called_with(deposit)
        )

    def test_stores_a_withdraw_transaction(self) -> None:
        withdraw = Amount(1000)
        transaction_repository = Mimic(Spy, InMemoryTransactionRepository)
        statement_printer = Mimic(Spy, StatementPrinter)
        account = Account(transaction_repository, statement_printer)

        account.withdraw(withdraw)

        expect(transaction_repository.add_withdraw).to(
            have_been_called_with(withdraw)
        )

    def test_prints_a_statement(self) -> None:
        with Mimic(
            Spy, InMemoryTransactionRepository
        ) as transaction_repository:
            transaction_repository.all_transactions().returns(
                [
                    Transaction(
                        TransactionType.DEPOSIT, "any-date", Amount(1000)
                    ),
                    Transaction(
                        TransactionType.WITHDRAW, "any-date", Amount(200)
                    ),
                ]
            )
        transactions: List[Transaction
                          ] = transaction_repository.all_transactions()
        statement_printer = Mimic(Spy, StatementPrinter)
        account = Account(transaction_repository, statement_printer)

        account.print_statement()

        expect(statement_printer.print).to(have_been_called_with(transactions))
