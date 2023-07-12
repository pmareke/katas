from src.domain.user_repository import UserRepository
from src.domain.user import User


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self.users: dict[str, User] = {}

    def save(self, user: User) -> None:
        self.users[user.email] = user

    def find_by_email(self, email_address: str) -> User | None:
        return self.users.get(email_address)
