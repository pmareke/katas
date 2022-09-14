from ohce.src.custom_clock import CustomClock
from ohce.src.console_output import ConsoleOutput


class Ohce:
    def __init__(self, console: ConsoleOutput, time: CustomClock):
        self.console = console
        self.time = time

    def run(self, user_name: str) -> None:
        self.console.print(f"¡Buenas noches {user_name}!")
