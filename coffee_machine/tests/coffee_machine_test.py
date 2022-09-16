from doublex import Mimic, Spy, Stub
from doublex_expects import have_been_called_with
from expects import expect

from coffee_machine.src.order_translator import OrderTranslator
from coffee_machine.src.drink_maker import DrinkMaker
from coffee_machine.src.printer import Printer
from coffee_machine.src.domain.order import Order
from coffee_machine.src.domain.drink import Coffee, Tea, Chocolate, Hot, OrangeJuice
from coffee_machine.coffee_machine import CoffeeMachine


class TestCoffeMachine:
    def test_makes_the_drinks(self) -> None:
        order_translator = OrderTranslator()
        drink_maker = Mimic(Spy, DrinkMaker)
        printer = Mimic(Stub, Printer)
        coffee_machine = CoffeeMachine(order_translator, drink_maker, printer)

        coffee_machine.add_money(money=0.4)
        order = Order(Tea(), sugar=1)
        coffee_machine.make_drink(order)

        expect(drink_maker.make).to(have_been_called_with("T:1:0"))

    def test_sends_a_message_with_missing_amount(self) -> None:
        order_translator = OrderTranslator()
        drink_maker = Mimic(Spy, DrinkMaker)
        printer = Mimic(Stub, Printer)
        coffee_machine = CoffeeMachine(order_translator, drink_maker, printer)

        coffee_machine.add_money(money=0.5)
        order = Order(Coffee(), sugar=1)
        coffee_machine.make_drink(order)

        expect(drink_maker.make).to(
            have_been_called_with(
                "M:Sorry there is not enough money in the cofee machine, you need 0.1 more."
            )
        )

    def test_prints_a_report(self) -> None:
        order_translator = OrderTranslator()
        drink_maker = DrinkMaker()
        printer = Mimic(Spy, Printer)
        coffee_machine = CoffeeMachine(order_translator, drink_maker, printer)
        tea = Order(Tea(), sugar=1)
        chocolate = Order(Chocolate(), sugar=0)
        orange_juice = Order(OrangeJuice(), sugar=0)
        coffee = Order(Coffee(), sugar=1)
        hot_coffee = Order(Hot(Coffee()), sugar=1)

        coffee_machine.add_money(money=10)
        coffee_machine.make_drink(tea)
        coffee_machine.make_drink(chocolate)
        coffee_machine.make_drink(orange_juice)
        coffee_machine.make_drink(coffee)
        coffee_machine.make_drink(hot_coffee)
        coffee_machine.create_report()

        expect(printer.print).to(have_been_called_with("1 Tea"))
        expect(printer.print).to(have_been_called_with("1 Chocolate"))
        expect(printer.print).to(have_been_called_with("1 Orange Juice"))
        expect(printer.print).to(have_been_called_with("2 Coffee"))
        expect(printer.print).to(have_been_called_with("Earned money: 2.7"))
