import pytest
from expects import equal, expect
from bank import Account


class TestBank:
    @pytest.mark.skip
    def test_adds_a_deposit(self) -> None:
        expected_output = [
            "date       || credit   || debit    || balance",
            "14/01/2012 ||          || 500.00   || 2500.00",
            "13/01/2012 || 2000.00  ||          || 3000.00",
            "10/01/2012 || 1000.00  ||          || 1000.00",
        ]

        account = Account()

        account.deposit(1000, "10/01/2012")
        account.deposit(2000, "13/01/2012")
        account.withdraw(500, "14/01/2012")

        expect(account.print_statement()).to(equal("\n".join(expected_output)))
