from doublex import Stub, Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect, contain

from ohce.src.ohce_runner import Ohce
from ohce.src.custom_clock import CustomClock
from ohce.src.console_output import ConsoleOutput


class TestOhce:
    any_user_name = "any-user-name"

    def test_greets_good_night(self) -> None:
        console_output = Mimic(Spy, ConsoleOutput)
        with Mimic(Stub, CustomClock) as custom_clock:
            custom_clock.time().returns("14/09/2022, 14:01:23")
        ohce = Ohce(console_output, custom_clock)

        ohce.run(self.any_user_name)

        expect(console_output.print).to(have_been_called_with(contain("Buenas noches")))
