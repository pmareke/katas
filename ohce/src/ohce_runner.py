from ohce.src.custom_clock import CustomClock
from ohce.src.console_output import ConsoleOutput


class Ohce:
    def __init__(self, console: ConsoleOutput, clock: CustomClock):
        self.console = console
        self.clock = clock

    def run(self, command: str) -> None:
        if command == "Stop!":
            response = f"Adios {command}"
        elif self._is_palindrome(command):
            response = "¡Bonita palabra!"
        elif self._is_night():
            response = f"!Buenas noches {command}¡"
        elif self._is_morning():
            response = f"!Buenos días {command}¡"
        elif self._is_afternoon():
            response = f"!Buenas tardes {command}¡"
        self.console.print(response)

    def _is_palindrome(self, command: str) -> bool:
        return command == "".join(reversed(command))

    def _is_night(self) -> bool:
        time = self.clock.time()
        return bool(time.hour >= 20 or time.hour < 6)

    def _is_morning(self) -> bool:
        time = self.clock.time()
        return bool(time.hour >= 6 and time.hour < 12)

    def _is_afternoon(self) -> bool:
        time = self.clock.time()
        return bool(time.hour >= 12 and time.hour < 20)
