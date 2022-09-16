from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect

from coffee_machine.src.order_translator import OrderTranslator
from coffee_machine.src.drink_maker import DrinkMaker
from coffee_machine.src.domain.order import Order
from coffee_machine.src.domain.drink import Coffee, Tea
from coffee_machine.coffee_machine import CoffeeMachine


class TestCoffeMachine:
    def test_makes_the_drinks(self) -> None:
        order_translator = OrderTranslator()
        drink_maker = Mimic(Spy, DrinkMaker)
        coffee_machine = CoffeeMachine(order_translator, drink_maker)

        coffee_machine.add_money(money=1)
        order = Order(Tea(), sugar=1)
        drink_maker_command = coffee_machine.translate_order(order)

        coffee_machine.make_drink(drink_maker_command)

        expect(drink_maker.make).to(have_been_called_with("T:1:0"))

    def test_sends_a_message_with_missing_amount(self) -> None:
        order_translator = OrderTranslator()
        drink_maker = Mimic(Spy, DrinkMaker)
        coffee_machine = CoffeeMachine(order_translator, drink_maker)

        coffee_machine.add_money(money=0.5)
        order = Order(Coffee(), sugar=1)
        drink_maker_command = coffee_machine.translate_order(order)

        coffee_machine.make_drink(drink_maker_command)

        expect(drink_maker.make).to(
            have_been_called_with(
                "M:Sorry there is not enough money in the cofee machine, you need 0.1 more."
            )
        )
