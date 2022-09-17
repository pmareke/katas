import pytest

from doublex import Spy, Stub
from doublex_expects import have_been_called_with
from expects import expect, raise_error

from coffee_machine.src.domain.checker import Checker
from coffee_machine.src.domain.notifier import Notifier
from coffee_machine.src.domain.printer import Printer
from coffee_machine.src.domain.maker import Maker
from coffee_machine.tests.coffee_machine_builder import CoffeeMachineBuilder
from coffee_machine.tests.test_data import TestData
from coffee_machine.coffee_machine import InvalidMoneyException


class TestCoffeMachine:
    def test_makes_the_drinks(self) -> None:
        tea_order = TestData.a_tea_order()
        maker = Spy(Maker)
        coffee_machine = CoffeeMachineBuilder().withMaker(maker).build()

        coffee_machine.add_money(money=0.4)
        coffee_machine.make_drink(tea_order)

        expect(maker.make).to(have_been_called_with("T:1:0"))

    @pytest.mark.parametrize("money", [-1.0, 0.0])
    def test_raises_and_error_with_invalid_money(self, money: float) -> None:
        maker = Spy(Maker)
        coffee_machine = CoffeeMachineBuilder().withMaker(maker).build()

        expect(lambda: coffee_machine.add_money(money=money)).to(
            raise_error(InvalidMoneyException)
        )

    def test_sends_a_message_with_missing_amount(self) -> None:
        coffee_order = TestData.a_coffee_order()
        maker = Spy(Maker)
        coffee_machine = CoffeeMachineBuilder().withMaker(maker).build()

        coffee_machine.add_money(money=0.5)
        coffee_machine.make_drink(coffee_order)

        expect(maker.make).to(
            have_been_called_with(
                "M:Sorry there is not enough money in the cofee machine, you need 0.1 more."
            )
        )

    def test_prints_a_report(self) -> None:
        orange_juice_order = TestData.an_orange_juice_order()
        printer = Spy(Printer)
        coffee_machine = CoffeeMachineBuilder().withPrinter(printer).build()

        coffee_machine.add_money(money=10)
        coffee_machine.make_drink(orange_juice_order)
        coffee_machine.create_report()

        expect(printer.print).to(have_been_called_with("1 OrangeJuice"))
        expect(printer.print).to(have_been_called_with("Earned money: 0.6"))

    def test_sends_an_email_when_there_is_a_shortage(self) -> None:
        tea_order = TestData.a_tea_order()
        notifier = Spy(Notifier)
        printer = Spy(Printer)
        with Stub(Checker) as beverage_quantity_checker:
            water = TestData.a_water()
            beverage_quantity_checker.is_empty(water).returns(True)
            milk = TestData.a_milk()
            beverage_quantity_checker.is_empty(milk).returns(False)
        coffee_machine_builder = (
            CoffeeMachineBuilder()
            .withNotifier(notifier)
            .withPrinter(printer)
            .withChecker(beverage_quantity_checker)
        )
        coffee_machine = coffee_machine_builder.build()

        coffee_machine.add_money(money=0.4)
        coffee_machine.make_drink(tea_order)

        expect(notifier.notify_missing_drink).to(have_been_called_with(water))
        expect(printer.print).to(
            have_been_called_with(
                f"There is a shortage with {water}, an email has been sent to refill the coffee machine."
            )
        )
        expect(notifier.notify_missing_drink).not_to(have_been_called_with(milk))
        expect(printer.print).not_to(
            have_been_called_with(
                f"There is a shortage with {milk}, an email has been sent to refill the coffee machine."
            )
        )
