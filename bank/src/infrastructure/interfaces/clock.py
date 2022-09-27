from abc import abstractmethod, ABC


class Clock(ABC):

    @abstractmethod
    def today(self) -> str:
        raise NotImplementedError
