from datetime import datetime

from doublex import Mimic, Stub, when
from ohce.src.custom_clock import CustomClock


class TestData:
    ANY_USER_NAME = "any-user-name"

    @staticmethod
    def a_custom_clock(date_time_str: str) -> CustomClock:
        custom_clock = Mimic(Stub, CustomClock)
        date = datetime.strptime(date_time_str, "%d/%m/%y %H:%M:%S")
        when(custom_clock).time().returns(date)
        return custom_clock
