from abc import ABC, abstractmethod


class Checker(ABC):

    @abstractmethod
    def is_empty(self, drink: str) -> bool:
        raise NotImplementedError
