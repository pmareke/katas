import json

from expects import be, be_none, equal, expect
from doublex import Mimic, Spy
from doublex_expects import have_been_called
from django.test import RequestFactory, TestCase

from src.domain.user import User
from src.infrastructure.smtp_email_sender import SmtpEmailSender
from src.infrastructure.user_framework_repository import InMemoryUserRepository
from src.framework.views import UserController
from src.use_cases.register_user import RegisterUser

class UserRegistrationControllerTestCase(TestCase):
    def setUp(self) -> None:
        self.user_repository = InMemoryUserRepository()
        self.email_sender = Mimic(Spy, SmtpEmailSender)
        register_user = RegisterUser(self.user_repository, self.email_sender)
        self.factory = RequestFactory()
        self.view = UserController.as_view(register_user=register_user)

    def test_should_success_when_everything_is_valid(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123'})

        response = self.view(request)

        expect(response.status_code).to(be(200))
        expect(self.email_sender.send).to(have_been_called)

    def test_should_returns_a_user_with_the_name_when_everything_is_valid(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123'})

        response = self.view(request)

        content = json.loads(response.content)
        expect(content["name"]).to(equal("Codium"))
        expect(self.email_sender.send).to(have_been_called)

    def test_should_returns_a_user_with_the_email_when_everything_is_valid(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123'})

        response = self.view(request)

        content = json.loads(response.content)
        expect(content["email"]).to(equal("info@codium.team"))
        expect(self.email_sender.send).to(have_been_called)

    def test_should_generate_a_random_id_when_everything_is_valid(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123'})

        response = self.view(request)

        content = json.loads(response.content)
        expect(content["id"]).not_to(be_none)
        expect(self.email_sender.send).to(have_been_called)

    def test_should_fail_when_password_is_short(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_'})

        response = self.view(request)

        expect(response.status_code).to(equal(400))
        expect(response.content).to(equal(b"Password is not valid"))
        expect(self.email_sender.send).not_to(have_been_called)

    def test_should_fail_when_password_does_not_contain_underscore(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass123123'})

        response = self.view(request)

        expect(response.status_code).to(equal(400))
        expect(response.content).to(equal(b"Password is not valid"))
        expect(self.email_sender.send).not_to(have_been_called)

    def test_persist_the_user(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123'})
        self.view(request)

        user = self.user_repository.find_by_email('info@codium.team')
        expect(user).not_to(be_none)
        expect(self.email_sender.send).to(have_been_called)

    def test_should_fail_when_email_is_used(self) -> None:

        self.user_repository.save(User(1, 'Codium', 'info@codium.team'))
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123'})
        response = self.view(request)

        expect(response.status_code).to(equal(400))
        expect(response.content).to(equal(b"The email is already in use"))
        expect(self.email_sender.send).not_to(have_been_called)
