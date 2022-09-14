import pytest

from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect

from ohce.src.ohce_runner import Ohce
from ohce.src.console_output import ConsoleOutput
from ohce.tests.test_data import TestData


class TestOhce:
    @pytest.mark.parametrize(
        "date",
        [
            "18/09/19 20:00:00",
            "18/09/19 00:10:19",
            "18/09/19 05:00:19",
        ],
    )
    def test_greets_good_night(self, date: str) -> None:
        console_input = TestData.a_console_input(TestData.ANY_WORD)
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock(date)
        ohce = Ohce(console_input, console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(
            have_been_called_with(f"!Buenas noches {TestData.ANY_USER_NAME}¡")
        )

    @pytest.mark.parametrize(
        "date",
        [
            "18/09/19 06:00:00",
            "18/09/19 08:55:19",
            "18/09/19 11:59:19",
        ],
    )
    def test_greets_good_morning(self, date: str) -> None:
        console_input = TestData.a_console_input(TestData.ANY_WORD)
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock(date)
        ohce = Ohce(console_input, console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(
            have_been_called_with(f"!Buenos días {TestData.ANY_USER_NAME}¡")
        )

    @pytest.mark.parametrize(
        "date",
        [
            "18/09/19 12:00:00",
            "18/09/19 15:25:19",
            "18/09/19 19:55:19",
        ],
    )
    def test_greets_good_afternoon(self, date: str) -> None:
        console_input = TestData.a_console_input(TestData.ANY_WORD)
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock(date)
        ohce = Ohce(console_input, console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(
            have_been_called_with(f"!Buenas tardes {TestData.ANY_USER_NAME}¡")
        )

    @pytest.mark.parametrize("word", ["oto", "radar", "refer", "kayak"])
    def test_greets_good_word_when_is_palindrome(self, word: str) -> None:
        console_input = TestData.a_console_input(word)
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock("18/09/19 10:50:00")
        ohce = Ohce(console_input, console_output, custom_clock)

        ohce.run(word)

        expect(console_output.print).to(
            have_been_called_with(TestData.reversed_word(word))
        )
        expect(console_output.print).to(have_been_called_with("!Bonita palabra¡"))

    @pytest.mark.parametrize("word", ["coche", "raton", "jabon"])
    def test_reverses_a_word(self, word: str) -> None:
        console_input = TestData.a_console_input(word)
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock("18/09/19 10:50:00")
        ohce = Ohce(console_input, console_output, custom_clock)

        ohce.run(word)

        expect(console_output.print).to(
            have_been_called_with(TestData.reversed_word(word))
        )
        expect(console_output.print).not_to(have_been_called_with("¡Bonita palabra!"))

    def test_says_goodbye(self) -> None:
        console_input = TestData.a_console_input("")
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock("18/09/19 10:50:00")
        ohce = Ohce(console_input, console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(
            have_been_called_with(f"Adios {TestData.ANY_USER_NAME}")
        )
