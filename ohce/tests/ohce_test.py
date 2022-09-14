import pytest

from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect, contain

from ohce.src.ohce_runner import Ohce
from ohce.src.console_output import ConsoleOutput
from ohce.src.custom_clock import CustomClock
from ohce.tests.test_data import TestData


class TestOhce:
    @pytest.mark.parametrize("date", ["18/09/19 01:55:19"])
    def test_greets_good_night(self, date: str) -> None:
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock(date)
        ohce = Ohce(console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(have_been_called_with(contain("Buenas noches")))

    @pytest.mark.parametrize("date", ["18/09/19 08:55:19"])
    def test_greets_good_morning(self, date: str) -> None:
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock(date)
        ohce = Ohce(console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(have_been_called_with(contain("Buenos días")))

    @pytest.mark.parametrize("date", ["18/09/19 18:55:19"])
    def test_greets_good_afternoon(self, date: str) -> None:
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock(date)
        ohce = Ohce(console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(have_been_called_with(contain("Buenas tardes")))

    @pytest.mark.parametrize("word", ["oto", "radar", "refer", "kayak"])
    def test_greets_good_word(self, word: str) -> None:
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = Mimic(Spy, CustomClock)
        ohce = Ohce(console_output, custom_clock)

        ohce.run(word)

        expect(console_output.print).to(
            have_been_called_with(contain("Bonita palabra"))
        )

    def test_says_goodbye(self) -> None:
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = Mimic(Spy, CustomClock)
        ohce = Ohce(console_output, custom_clock)

        ohce.run("Stop!")

        expect(console_output.print).to(have_been_called_with(contain("Adios")))
