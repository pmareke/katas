from random import randint

from src.domain.email_sender import EmailSender
from src.domain.exceptions import EmailAlreadyInUseException, InvalidPasswordException
from src.domain.user import User
from src.domain.user_repository import UserRepository


class RegisterUser:
    def __init__(self, user_repository: UserRepository, email_sender: EmailSender) -> None:
        self.user_repository = user_repository
        self.email_sender = email_sender

    def execute(self, name: str, password: str, email: str) -> dict:
        if len(password) <= 8 or "_" not in password:
            raise InvalidPasswordException
        if self.user_repository.find_by_email(email) is not None:
            raise EmailAlreadyInUseException

        user = User(randint(1, 999999), name, email)
        self.user_repository.save(user)

        from_email = "info@codium.team"
        subject = "Confirmation Link"
        self.email_sender.send(from_email, email, subject)

        return {'name': user.name, 'email': user.email, 'id': user.user_id}
