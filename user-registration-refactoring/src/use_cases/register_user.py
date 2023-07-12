import smtplib
import ssl
from random import randint

from src.domain.exceptions import EmailAlreadyInUseException, InvalidPasswordException
from src.domain.user import User
from src.infrastructure.user_framework_repository import UserFrameworkRepository


class RegisterUser:
    def __init__(self, user_repository: UserFrameworkRepository) -> None:
        self.user_repository = user_repository

    def execute(self, name: str, password: str, email: str) -> dict:
        if len(password) <= 8:
            raise InvalidPasswordException
        if "_" not in password:
            raise InvalidPasswordException
        if self.user_repository.find_by_email(email) is not None:
            raise EmailAlreadyInUseException

        user = self._create_user(name, email)
        self._send_email()

        return {'name': user.name, 'email': user.email, 'id': user.user_id}

    def _create_user(self, name: str, email: str) -> User:
        user = User(randint(1, 999999), name, email)
        self.user_repository.save(user)
        return user

    def _send_email(self) -> None:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context):
            pass
            # Uncomment this lines with a valid username and password
            # server.login("my@gmail.com", "myPassword")
            # server.sendmail('info@codium.team', request.POST['email'], 'Confirmation link')
