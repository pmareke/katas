from src.domain.user import User


class UserFrameworkRepository:
    def __init__(self) -> None:
        self.users: dict[str, User] = {}
        self.repository: "UserFrameworkRepository" | None = None

    def save(self, user: User) -> None:
        self.users[user.email] = user

    def find_by_email(self, email_address: str) -> User | None:
        return self.users.get(email_address)
