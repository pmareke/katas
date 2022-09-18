from doublex import Stub, Spy

from coffee_machine.src.domain.notifier import Notifier
from coffee_machine.src.domain.checker import Checker
from coffee_machine.src.domain.printer import Printer
from coffee_machine.src.infrastructure.email_notifier import EmailNotifier


class NotifierBuilder:
    def __init__(self) -> None:
        self.printer = Spy(Printer)
        self.checker = Stub(Checker)

    def with_printer(self, printer: Printer) -> "NotifierBuilder":
        self.printer = printer
        return self

    def with_checker(self, checker: Checker) -> "NotifierBuilder":
        self.checker = checker
        return self

    def build(self) -> Notifier:
        return EmailNotifier(self.printer, self.checker)
