from src.domain.user import User


class UserFrameworkRepository:
    repository: "UserFrameworkRepository" | None = None

    def __init__(self) -> None:
        self.users: dict[str, User] = {}

    def save(self, user: User) -> None:
        self.users[user.email] = user

    def find_by_email(self, email_address: str) -> User | None:
        return self.users.get(email_address)

    @staticmethod
    def get_instance() -> "UserFrameworkRepository":
        if UserFrameworkRepository.repository is None:
            UserFrameworkRepository.repository = UserFrameworkRepository()
        return UserFrameworkRepository.repository

    @staticmethod
    def set_instance(the_instance: "UserFrameworkRepository") -> None:
        UserFrameworkRepository.repository = the_instance
