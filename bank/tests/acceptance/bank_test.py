from doublex import Mimic, Mock, Stub
from doublex_expects import have_been_satisfied
from expects import expect
from bank.src.bank import Account
from bank.src.console import Console
from bank.src.transaction_repository import TransactionRepository
from bank.src.statement_printer import StatementPrinter
from bank.src.clock import Clock


class TestBank:
    def test_prints_the_statements(self) -> None:
        with Mimic(Stub, Clock) as clock:
            clock.today().delegates(["12/01/2012", "13/01/2012", "14/01/2012"])
        with Mimic(Mock, Console) as console:
            console.print_line("date || credit || debit || balance")
            console.print_line("14/01/2012 || 2000.00 || || 2800.00")
            console.print_line("13/01/2012 || || 200.00 || 800.00")
            console.print_line("12/01/2012 || 1000.00 || || 1000.00")
        transaction_repository = TransactionRepository(clock)
        statement_printer = StatementPrinter(console)
        account = Account(transaction_repository, statement_printer)

        account.deposit(1000)
        account.withdraw(200)
        account.deposit(2000)

        account.print_statement()

        expect(console).to(have_been_satisfied)
