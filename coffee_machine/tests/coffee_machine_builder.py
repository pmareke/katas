from doublex import Spy

from coffee_machine.coffee_machine import CoffeeMachine
from coffee_machine.src.infrastructure.order_translator import OrderTranslator
from coffee_machine.src.domain.translator import Translator
from coffee_machine.src.domain.maker import Maker
from coffee_machine.src.domain.printer import Printer
from coffee_machine.src.domain.notifier import Notifier
from coffee_machine.src.domain.checker import Checker


class CoffeeMachineBuilder:
    def __init__(self) -> None:
        self.order_translator = OrderTranslator()
        self.drink_maker = Spy(Maker)
        self.printer = Spy(Printer)
        self.notifier = Spy(Notifier)
        self.checker = Spy(Checker)

    def withOrderTranslator(
        self, order_translator: Translator
    ) -> "CoffeeMachineBuilder":
        self.order_translator = order_translator
        return self

    def withDrinkMaker(self, drink_maker: Maker) -> "CoffeeMachineBuilder":
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
