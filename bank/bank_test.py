import pytest
from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect
from bank.bank import Account


class TestBank:
    @pytest.mark.skip
    def test_adds_a_deposit(self) -> None:
        account = Account()
        printer = Spy()

        account.deposit(1000)
        account.deposit(2000)
        account.withdraw(500)

        account.print_statement()

        expect(printer.print).to(
            have_been_called_with("date       || credit   || debit    || balance")
        )
        expect(printer.print).to(
            have_been_called_with("14/01/2012 ||          || 500.00   || 2500.00")
        )
        expect(printer.print).to(
            have_been_called_with("13/01/2012 || 2000.00  ||          || 3000.00")
        )
        expect(printer.print).to(
            have_been_called_with("10/01/2012 || 1000.00  ||          || 1000.00")
        )
