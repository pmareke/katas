from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect

from ohce.src.ohce_runner import Ohce
from ohce.src.console_output import ConsoleOutput
from ohce.tests.test_data import TestData


class TestOhceAcceptance:
    def test_runs_ohce_in_the_morning(self) -> None:
        console_input = TestData.a_console_input(TestData.ANY_WORD)
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock("10/10/10 10:10:10")
        ohce = Ohce(console_input, console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(
            have_been_called_with(f"!Buenos días {TestData.ANY_USER_NAME}¡")
        )
        expect(console_output.print).to(have_been_called_with(TestData.reversed_word()))
        expect(console_output.print).to(
            have_been_called_with(f"Adios {TestData.ANY_USER_NAME}")
        )

    def test_runs_ohce_in_the_night(self) -> None:
        console_input = TestData.a_console_input(TestData.ANY_WORD)
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock("10/10/10 20:10:10")
        ohce = Ohce(console_input, console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(
            have_been_called_with(f"!Buenas noches {TestData.ANY_USER_NAME}¡")
        )
        expect(console_output.print).to(have_been_called_with(TestData.reversed_word()))
        expect(console_output.print).to(
            have_been_called_with(f"Adios {TestData.ANY_USER_NAME}")
        )

    def test_runs_ohce_in_the_afternoon(self) -> None:
        console_input = TestData.a_console_input(TestData.ANY_WORD)
        console_output = Mimic(Spy, ConsoleOutput)
        custom_clock = TestData.a_custom_clock("10/10/10 15:10:10")
        ohce = Ohce(console_input, console_output, custom_clock)

        ohce.run(TestData.ANY_USER_NAME)

        expect(console_output.print).to(
            have_been_called_with(f"!Buenas tardes {TestData.ANY_USER_NAME}¡")
        )
        expect(console_output.print).to(have_been_called_with(TestData.reversed_word()))
        expect(console_output.print).to(
            have_been_called_with(f"Adios {TestData.ANY_USER_NAME}")
        )
