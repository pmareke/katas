from ohce.src.custom_clock import CustomClock
from ohce.src.console_output import ConsoleOutput


class Ohce:
    def __init__(self, console: ConsoleOutput, clock: CustomClock):
        self.console = console
        self.clock = clock

    def run(self, user_name: str) -> None:
        if self._is_night():
            message = f"!Buenas noches {user_name}¡"
        elif self._is_morning():
            message = f"!Buenos días {user_name}¡"
        elif self._is_afternoon():
            message = f"!Buenas tardes {user_name}¡"
        self.console.print(message)

    def _is_night(self) -> bool:
        time = self.clock.time()
        return bool(time.hour >= 20 or time.hour < 6)

    def _is_morning(self) -> bool:
        time = self.clock.time()
        return bool(time.hour >= 6 and time.hour < 12)

    def _is_afternoon(self) -> bool:
        time = self.clock.time()
        return bool(time.hour >= 12 and time.hour < 20)
