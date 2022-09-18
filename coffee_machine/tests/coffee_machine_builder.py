from doublex import Spy

from coffee_machine.use_cases.coffee_machine_command_handler import (
    CoffeeMachineCommandHandler,
)
from coffee_machine.src.infrastructure.order_translator import OrderTranslator
from coffee_machine.src.domain.translator import Translator
from coffee_machine.src.domain.maker import Maker
from coffee_machine.src.domain.printer import Printer
from coffee_machine.src.domain.notifier import Notifier
from coffee_machine.src.domain.checker import Checker


class CoffeeMachineCommandHandlerBuilder:
    def __init__(self) -> None:
        self.translator = OrderTranslator()
        self.maker = Spy(Maker)
        self.printer = Spy(Printer)
        self.notifier = Spy(Notifier)
        self.checker = Spy(Checker)

    def with_translator(
        self, translator: Translator
    ) -> "CoffeeMachineCommandHandlerBuilder":
        self.translator = translator
        return self

    def with_maker(self, maker: Maker) -> "CoffeeMachineCommandHandlerBuilder":
        self.maker = maker
        return self

    def with_printer(self, printer: Printer) -> "CoffeeMachineCommandHandlerBuilder":
        self.printer = printer
        return self

    def with_notifier(self, notifier: Notifier) -> "CoffeeMachineCommandHandlerBuilder":
        self.notifier = notifier
        return self

    def with_checker(self, checker: Checker) -> "CoffeeMachineCommandHandlerBuilder":
        self.checker = checker
        return self

    def build(self) -> CoffeeMachineCommandHandler:
        return CoffeeMachineCommandHandler(
            self.translator,
            self.maker,
            self.printer,
            self.notifier,
            self.checker,
        )
