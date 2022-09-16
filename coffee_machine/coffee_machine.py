from typing import Dict
from coffee_machine.src.domain.order import Order
from coffee_machine.src.domain.drink import Drink, Coffee, Chocolate, Tea, OrangeJuice
from coffee_machine.src.order_translator import OrderTranslator
from coffee_machine.src.printer import Printer
from coffee_machine.src.drink_maker import DrinkMaker


class CoffeeMachine:
    def __init__(
        self,
        order_translator: OrderTranslator,
        drink_maker: DrinkMaker,
        printer: Printer,
    ):
        self.order_translator = order_translator
        self.drink_maker = drink_maker
        self.printer = printer
        self.money = 0.0
        self.items_sell_by_type: Dict[Drink, int] = {}

    def add_money(self, money: float) -> None:
        self.money = money

    def make_drink(self, order: Order) -> None:
        command = self._translate_order(order)
        self.drink_maker.make(command)
        if not command.startswith("M"):
            drink_initial = order.drink.initial
            current_value = self.items_sell_by_type.get(drink_initial, 0)
            self.items_sell_by_type[drink_initial] = current_value + 1

    def create_report(self) -> None:
        earned_money = 0.0
        for drink_initial, times in self.items_sell_by_type.items():
            drink = self._get_drink_from_initial(drink_initial)
            earned_money += drink.price * times
            self.printer.print(f"{times} {drink}")
        self.printer.print(f"Earned money: {earned_money}")

    def _translate_order(self, order: Order) -> str:
        if self.money >= order.drink.price:
            return str(self.order_translator.translate(order))

        missing_money = round(abs(self.money - order.drink.price), 2)
        error_message = f"Sorry there is not enough money in the cofee machine, you need {missing_money} more."
        self.money -= order.drink.price
        return f"M:{error_message}"

    def _get_drink_from_initial(self, drink_initial: str) -> Drink:
        return {
            "C": Coffee(),
            "T": Tea(),
            "H": Chocolate(),
            "O": OrangeJuice(),
        }[drink_initial]
