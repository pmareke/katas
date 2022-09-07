from abc import ABC


class Clock(ABC):
    def today(self) -> str:
        raise NotImplementedError
