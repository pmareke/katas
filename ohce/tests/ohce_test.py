from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect, contain

from ohce.src.ohce_runner import Ohce
from ohce.src.console_output import ConsoleOutput
from ohce.tests.test_data import TestData


class TestOhce:
    def test_greets_good_night(self) -> None:
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock("18/09/19 01:55:19")
        ohce = Ohce(console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(have_been_called_with(contain("Buenas noches")))

    def test_greets_good_morning(self) -> None:
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock("18/09/19 08:55:19")
        ohce = Ohce(console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(have_been_called_with(contain("Buenos días")))

    def test_greets_good_afternoon(self) -> None:
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock("18/09/19 18:55:19")
        ohce = Ohce(console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(have_been_called_with(contain("Buenas tardes")))
