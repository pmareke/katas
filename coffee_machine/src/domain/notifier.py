from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def notify_missing_drink(self, drink: str) -> None:
        raise NotImplementedError
