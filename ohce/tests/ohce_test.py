from datetime import datetime
from doublex import Stub, Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect, contain

from ohce.src.ohce_runner import Ohce
from ohce.src.custom_clock import CustomClock
from ohce.src.console_output import ConsoleOutput


class TestOhce:
    def test_greets_good_night(self) -> None:
        console_output = Mimic(Spy, ConsoleOutput)
        with Mimic(Stub, CustomClock) as custom_clock:
            date_time_str = "18/09/19 01:55:19"
            date = datetime.strptime(date_time_str, "%d/%m/%y %H:%M:%S")
            custom_clock.time().returns(date)
        ohce = Ohce(console_output, custom_clock)

        ohce.run("any-user-name")

        expect(console_output.print).to(have_been_called_with(contain("Buenas noches")))

    def test_greets_good_morning(self) -> None:
        console_output = Mimic(Spy, ConsoleOutput)
        with Mimic(Stub, CustomClock) as custom_clock:
            date_time_str = "18/09/19 08:55:19"
            date = datetime.strptime(date_time_str, "%d/%m/%y %H:%M:%S")
            custom_clock.time().returns(date)
        ohce = Ohce(console_output, custom_clock)

        ohce.run("any-user-name")

        expect(console_output.print).to(have_been_called_with(contain("Buenos días")))

    def test_greets_good_afternoon(self) -> None:
        console_output = Mimic(Spy, ConsoleOutput)
        with Mimic(Stub, CustomClock) as custom_clock:
            date_time_str = "18/09/19 18:55:19"
            date = datetime.strptime(date_time_str, "%d/%m/%y %H:%M:%S")
            custom_clock.time().returns(date)
        ohce = Ohce(console_output, custom_clock)

        ohce.run("any-user-name")

        expect(console_output.print).to(have_been_called_with(contain("Buenas tardes")))
