from datetime import datetime

from bank.src.infrastructure.interfaces.clock import Clock


class DatetimeClock(Clock):
    def today(self) -> str:
        return str(datetime.today().strftime("%d-%m-%Y"))
