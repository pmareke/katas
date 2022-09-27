from ohce.src.custom_clock import CustomClock
from ohce.src.console_output import ConsoleOutput
from ohce.src.console_input import ConsoleInput


class Ohce:
    _GOOD_NIGHT_GREETING = "Buenas noches"
    _GOOD_MORNING_GREETING = "Buenos días"
    _GOOD_AFTERNOON_GREETING = "Buenas tardes"
    _PALINDROME_GREETING = "Bonita palabra"
    _BYE_GREETING = "Adios"
    _STOP_COMMAND = "Stop!"
    _START_MORNING_HOUR = 6
    _START_AFTERNOON_HOUR = 12
    _START_NIGHT_HOUR = 20

    def __init__(
        self,
        console_input: ConsoleInput,
        console_output: ConsoleOutput,
        clock: CustomClock,
    ):
        self.console_input = console_input
        self.console_output = console_output
        self.clock = clock
        self.time = self.clock.time()

    def run(self, user_name: str) -> None:
        greet = self._generate_greet_for_user(user_name)
        self.console_output.print(f"!{greet} {user_name}¡")

        while (command := self.console_input.input()) != self._STOP_COMMAND:
            self.console_output.print(self._reverse_word(command))
            if self._is_palindrome(user_name):
                self.console_output.print(f"!{self._PALINDROME_GREETING}¡")

        self.console_output.print(f"{self._BYE_GREETING} {user_name}")

    # PRIVATE METHODS

    def _generate_greet_for_user(self, user_name: str) -> str:
        if self._is_night():
            return self._GOOD_NIGHT_GREETING
        if self._is_morning():
            return self._GOOD_MORNING_GREETING
        return self._GOOD_AFTERNOON_GREETING

    def _is_palindrome(self, word: str) -> bool:
        return word == self._reverse_word(word)

    def _reverse_word(self, word: str) -> str:
        return "".join(reversed(word))

    def _is_night(self) -> bool:
        return bool(self.time.hour >= self._START_NIGHT_HOUR
                    or self.time.hour < self._START_MORNING_HOUR)

    def _is_morning(self) -> bool:
        return bool(self.time.hour >= self._START_MORNING_HOUR
                    and self.time.hour < self._START_AFTERNOON_HOUR)
