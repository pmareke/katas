from abc import ABC, abstractmethod


class Output(ABC):
    @abstractmethod
    def print_line(self, line: str) -> None:
        raise NotImplementedError
