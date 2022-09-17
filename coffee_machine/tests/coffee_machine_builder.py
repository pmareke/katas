from doublex import Mimic, Spy

from coffee_machine.coffee_machine import CoffeeMachine
from coffee_machine.src.infrastructure.order_translator import OrderTranslator
from coffee_machine.src.infrastructure.drink_maker import DrinkMaker
from coffee_machine.src.infrastructure.printer import Printer
from coffee_machine.src.infrastructure.email_notifier import EmailNotifier
from coffee_machine.src.infrastructure.beverage_quantity_checker import (
    BeverageQuantityChecker,
)
from coffee_machine.src.domain.notifier import Notifier
from coffee_machine.src.domain.checker import Checker


class CoffeeMachineBuilder:
    def __init__(self) -> None:
        self.order_translator = OrderTranslator()
        self.drink_maker = Mimic(Spy, DrinkMaker)
        self.printer = Mimic(Spy, Printer)
        self.notifier = Mimic(Spy, EmailNotifier)
        self.checker = Mimic(Spy, BeverageQuantityChecker)

    def withOrderTranslator(
        self, order_translator: OrderTranslator
    ) -> "CoffeeMachineBuilder":
        self.order_translator = order_translator
        return self

    def withDrinkMaker(self, drink_maker: DrinkMaker) -> "CoffeeMachineBuilder":
        self.drink_maker = drink_maker
        return self

    def withPrinter(self, printer: Printer) -> "CoffeeMachineBuilder":
        self.printer = printer
        return self

    def withNotifier(self, notifier: Notifier) -> "CoffeeMachineBuilder":
        self.notifier = notifier
        return self

    def withChecker(self, checker: Checker) -> "CoffeeMachineBuilder":
        self.checker = checker
        return self

    def build(self) -> CoffeeMachine:
        return CoffeeMachine(
            self.order_translator,
            self.drink_maker,
            self.printer,
            self.notifier,
            self.checker,
        )
