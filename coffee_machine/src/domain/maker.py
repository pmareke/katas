from abc import ABC, abstractmethod


class Maker(ABC):
    @abstractmethod
    def make(self, command: str) -> None:
        raise NotImplementedError
