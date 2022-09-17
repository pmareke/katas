from coffee_machine.src.domain.printer import Printer


class CustomPrinter(Printer):
    def print(self, message: str) -> None:
        print(message)
