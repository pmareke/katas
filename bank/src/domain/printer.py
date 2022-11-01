from abc import abstractmethod, ABC

from bank.src.domain.transaction import Transaction


class Printer(ABC):

    @abstractmethod
    def print(self, transactions: list[Transaction]) -> None:
        raise NotImplementedError
