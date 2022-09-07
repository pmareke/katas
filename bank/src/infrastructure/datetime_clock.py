from datetime import datetime

from bank.src.domain.clock import Clock


class DatetimeClock(Clock):
    def today(self) -> str:
        return str(datetime.today().strftime("%d-%m-%Y"))
