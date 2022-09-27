from expects import expect, raise_error, equal

from coffee_machine.src.domain.money import Money, InvalidMoneyException


class TestMoney:

    def test_creates_money(self) -> None:
        money = Money(2.0)

        expect(money.value).to(equal(2.0))

    def test_raises_and_error_with_invalid_money(self) -> None:
        expect(lambda: Money(-1.0)).to(raise_error(InvalidMoneyException))
