from abc import ABC, abstractmethod

from src.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email_address: str) -> User | None:
        raise NotImplementedError
