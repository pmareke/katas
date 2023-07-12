from abc import ABC, abstractmethod


class EmailSender(ABC):
    @abstractmethod
    def send(self, from_email: str, to_email: str, subject: str) -> None:
        raise NotImplementedError
