from typing import Dict
from coffee_machine.src.domain.order import Order
from coffee_machine.src.domain.drink import (
    Drink,
    Coffee,
    Chocolate,
    Tea,
    OrangeJuice,
    Milk,
    Water,
)
from coffee_machine.src.domain.notifier import Notifier
from coffee_machine.src.domain.translator import Translator
from coffee_machine.src.domain.printer import Printer
from coffee_machine.src.domain.checker import Checker
from coffee_machine.src.domain.maker import Maker
from coffee_machine.src.domain.money import Money


class InsufficientMoneyException(Exception):
    pass


class CoffeeMachineCommandHandler:
    shortage_drinks = [Water(), Milk()]

    def __init__(
        self,
        order_translator: Translator,
        drink_maker: Maker,
        printer: Printer,
        notifier: Notifier,
        checker: Checker,
    ):
        self.order_translator = order_translator
        self.drink_maker = drink_maker
        self.printer = printer
        self.notifier = notifier
        self.checker = checker
        self.money = Money(0)
        self.items_sell_by_type: Dict[Drink, int] = {}

    def add_money(self, money: Money) -> None:
        self.money = money

    def make_drink(self, order: Order) -> None:
        self._check_shortage()
        try:
            command = self._translate_order(order)
            self._update_sent_drinks(order)
        except InsufficientMoneyException as exception:
            command = str(exception)
        self.drink_maker.make(command)

    def _check_shortage(self) -> None:
        for drink in self.shortage_drinks:
            if self.checker.is_empty(drink):
                error_message = f"There is a shortage with {drink}, an email has been sent to refill the coffee machine."
                self.printer.print(error_message)
                self.notifier.notify_missing_drink(drink)

    def _translate_order(self, order: Order) -> str:
        if self.money.value < order.drink.price:
            missing_money = Money(abs(self.money.value - order.drink.price))
            error_message = f"M:Sorry there is not enough money in the coffee machine, you need {missing_money} more."
            raise InsufficientMoneyException(error_message)

        return str(self.order_translator.translate(order))

    def _update_sent_drinks(self, order: Order) -> None:
        drink_initial = order.drink.initial
        current_value = self.items_sell_by_type.get(drink_initial, 0)
        self.items_sell_by_type[drink_initial] = current_value + 1

    def create_report(self) -> None:
        earned_money = Money(0)
        for drink_initial, times in self.items_sell_by_type.items():
            drink = self._get_drink_from_initial(drink_initial)
            earned_money.add_money(Money(drink.price * times))
            self.printer.print(f"{times} {drink}")
        self.printer.print(f"Earned money: {earned_money.value}")

    def _get_drink_from_initial(self, drink_initial: str) -> Drink:
        return {
            "C": Coffee(),
            "T": Tea(),
            "H": Chocolate(),
            "O": OrangeJuice(),
        }[drink_initial]
