from expects import be_false, be_true, expect
import pytest

from leap_year import LeapYear


class TestLeapYear:
    @pytest.mark.parametrize("year", [1996, 1600, 1804, 2144, 2384, 2000])
    def test_year_1996_is_leap_year(self, year: int):
        expect(LeapYear().calculate(year)).to(be_true)

    @pytest.mark.parametrize(
        "year", [1997, 1800, 1900, 2100, 2200, 2300, 2500, 2600, 2700, 2900, 3000]
    )
    def test_year_1997_is_not_leap_year(self, year: int):
        expect(LeapYear().calculate(year)).to(be_false)
