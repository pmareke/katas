from leap_year import LeapYear


class TestLeapYear:
    def test_is_leap_year(self):
        assert LeapYear().calculate(0) == False
