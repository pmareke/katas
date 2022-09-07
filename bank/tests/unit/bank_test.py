from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect
from typing import List

from bank.src.bank import Account
from bank.src.transaction_repository import TransactionRepository
from bank.src.statement_printer import StatementPrinter
from bank.src.transaction import Transaction, TransactionType


class TestBank:
    def test_stores_a_deposit_transaction(self) -> None:
        deposit = 1000
        transaction_repository = Mimic(Spy, TransactionRepository)
        statement_printer = Mimic(Spy, StatementPrinter)
        account = Account(transaction_repository, statement_printer)

        account.deposit(deposit)

        expect(transaction_repository.add_deposit).to(have_been_called_with(deposit))

    def test_stores_a_withdraw_transaction(self) -> None:
        withdraw = 1000
        transaction_repository = Mimic(Spy, TransactionRepository)
        statement_printer = Mimic(Spy, StatementPrinter)
        account = Account(transaction_repository, statement_printer)

        account.withdraw(withdraw)

        expect(transaction_repository.add_withdraw).to(have_been_called_with(withdraw))

    def test_prints_a_statement(self) -> None:
        with Mimic(Spy, TransactionRepository) as transaction_repository:
            transaction_repository.all_transactions().returns(
                [Transaction(TransactionType.DEPOSIT, "any-date", 0)]
            )
        transactions: List[Transaction] = transaction_repository.all_transactions()
        statement_printer = Mimic(Spy, StatementPrinter)
        account = Account(transaction_repository, statement_printer)

        account.print_statement()

        expect(statement_printer.print).to(have_been_called_with(transactions))
