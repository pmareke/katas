from abc import ABC, abstractmethod

from coffee_machine.src.domain.order import Order


class Translator(ABC):
    @abstractmethod
    def translate(self, order: Order) -> str:
        raise NotImplementedError
