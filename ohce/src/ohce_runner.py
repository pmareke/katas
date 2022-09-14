from ohce.src.custom_clock import CustomClock
from ohce.src.console_output import ConsoleOutput
from ohce.src.console_input import ConsoleInput


class Ohce:
    def __init__(
        self,
        console_input: ConsoleInput,
        console_output: ConsoleOutput,
        clock: CustomClock,
    ):
        self.console_input = console_input
        self.console_output = console_output
        self.clock = clock

    def run(self, user_name: str) -> None:
        self._greet_user(user_name)

        while (command := self.console_input.input()) != "Stop!":
            self.console_output.print(self._reverse_word(command))
            if self._is_palindrome(user_name):
                self.console_output.print("!Bonita palabra¡")

        self.console_output.print(f"Adios {user_name}")

    def _greet_user(self, user_name: str) -> None:
        if self._is_night():
            response = f"!Buenas noches {user_name}¡"
            self.console_output.print(response)
        elif self._is_morning():
            response = f"!Buenos días {user_name}¡"
            self.console_output.print(response)
        elif self._is_afternoon():
            response = f"!Buenas tardes {user_name}¡"
            self.console_output.print(response)

    def _is_palindrome(self, command: str) -> bool:
        return command == "".join(reversed(command))

    def _reverse_word(self, word: str) -> str:
        return "".join(reversed(word))

    def _is_night(self) -> bool:
        time = self.clock.time()
        return bool(time.hour >= 20 or time.hour < 6)

    def _is_morning(self) -> bool:
        time = self.clock.time()
        return bool(time.hour >= 6 and time.hour < 12)

    def _is_afternoon(self) -> bool:
        time = self.clock.time()
        return bool(time.hour >= 12 and time.hour < 20)
