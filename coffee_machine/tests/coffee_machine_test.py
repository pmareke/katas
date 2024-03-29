from doublex import Spy, Stub
from doublex_expects import have_been_called_with
from expects import expect

from coffee_machine.src.domain.checker import Checker
from coffee_machine.src.domain.printer import Printer
from coffee_machine.src.domain.notifier import Notifier
from coffee_machine.src.domain.maker import Maker
from coffee_machine.src.domain.money import Money
from coffee_machine.tests.coffee_machine_builder import (
    CoffeeMachineCommandHandlerBuilder, )
from coffee_machine.tests.test_data import TestData


class TestCoffeMachine:

    def test_makes_the_drinks(self) -> None:
        tea_order = TestData.a_tea_order()
        maker = Spy(Maker)
        command_handler = CoffeeMachineCommandHandlerBuilder().with_maker(
            maker).build()

        command_handler.add_money(money=Money(0.4))
        command_handler.make_drink(tea_order)

        expect(maker.make).to(have_been_called_with("T:1:0"))

    def test_sends_a_message_with_missing_amount(self) -> None:
        coffee_order = TestData.a_coffee_order()
        maker = Spy(Maker)
        command_handler = CoffeeMachineCommandHandlerBuilder().with_maker(
            maker).build()

        command_handler.add_money(money=Money(0.5))
        command_handler.make_drink(coffee_order)

        expect(maker.make).to(
            have_been_called_with(
                "M:Sorry there is not enough money in the coffee machine, you need 0.1 more."
            ))

    def test_prints_a_report(self) -> None:
        orange_juice_order = TestData.an_orange_juice_order()
        printer = Spy(Printer)
        command_handler = (
            CoffeeMachineCommandHandlerBuilder().with_printer(printer).build())

        command_handler.add_money(money=Money(10))
        command_handler.make_drink(orange_juice_order)
        command_handler.create_report()

        expect(printer.print).to(have_been_called_with("1 OrangeJuice"))
        expect(printer.print).to(have_been_called_with("Earned money: 0.6"))

    def test_sends_an_email_when_there_is_a_shortage(self) -> None:
        tea_order = TestData.a_tea_order()
        notifier = Spy(Notifier)
        with Stub(Checker) as checker:
            water = TestData.a_water()
            checker.is_empty(water).returns(True)
            milk = TestData.a_milk()
            checker.is_empty(milk).returns(False)
        command_handler = (CoffeeMachineCommandHandlerBuilder().with_notifier(
            notifier).with_checker(checker).build())

        command_handler.add_money(money=Money(0.4))
        command_handler.make_drink(tea_order)

        expect(notifier.notify_missing_drink).to(have_been_called_with(water))
        expect(notifier.notify_missing_drink).not_to(
            have_been_called_with(milk))

    def test_prints_a_message_when_there_is_a_shortage(self) -> None:
        tea_order = TestData.a_tea_order()
        printer = Spy(Printer)
        with Stub(Checker) as checker:
            water = TestData.a_water()
            checker.is_empty(water).returns(True)
            milk = TestData.a_milk()
            checker.is_empty(milk).returns(False)
        command_handler = (CoffeeMachineCommandHandlerBuilder().with_printer(
            printer).with_checker(checker).build())

        command_handler.add_money(money=Money(0.4))
        command_handler.make_drink(tea_order)

        expect(printer.print).to(
            have_been_called_with(
                f"There is a shortage with {water}, an email has been sent to refill the coffee machine."
            ))
        expect(printer.print).not_to(
            have_been_called_with(
                f"There is a shortage with {milk}, an email has been sent to refill the coffee machine."
            ))
