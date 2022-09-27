from datetime import datetime


class CustomClock:

    def time(self) -> datetime:
        return datetime.now()
