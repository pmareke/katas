from datetime import datetime


class Clock:
    def today(self) -> str:
        return str(datetime.today().strftime("%d-%m-%Y"))
