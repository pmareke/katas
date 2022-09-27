from expects import expect, equal

from bank.src.infrastructure.datetime_clock import DatetimeClock


class DummyClock(DatetimeClock):

    def today(self) -> str:
        return "12/01/2012"


class TestClock:

    def test_returns_today_as_string_DD_MM_YYYY(self) -> None:
        clock = DummyClock()

        date = clock.today()

        expect(date).to(equal("12/01/2012"))
