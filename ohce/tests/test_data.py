from datetime import datetime

from doublex import Mimic, Stub, when
from ohce.src.custom_clock import CustomClock
from ohce.src.console_input import ConsoleInput


class TestData:
    ANY_USER_NAME = "any-user-name"
    ANY_WORD = "any-word"

    @staticmethod
    def reversed_word(word: str = ANY_WORD) -> str:
        return "".join(reversed(word))

    @staticmethod
    def a_console_input(command: str) -> ConsoleInput:
        console_input = Mimic(Stub, ConsoleInput)
        when(console_input).input().delegates([command, "Stop!"])
        return console_input

    @staticmethod
    def a_custom_clock(date_time_str: str) -> CustomClock:
        custom_clock = Mimic(Stub, CustomClock)
        date = datetime.strptime(date_time_str, "%d/%m/%y %H:%M:%S")
        when(custom_clock).time().returns(date)
        return custom_clock
