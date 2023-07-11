import json

from django.test import RequestFactory, TestCase
from src.domain.user import User
from src.infrastructure.user_framework_repository import UserFrameworkRepository
from src.framework.views import UserController

class UserRegistrationControllerTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.view = UserController.as_view()

    def test_should_success_when_everything_is_valid(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123'})

        response = self.view(request)

        self.assertEqual(response.status_code, 200)

    def test_should_returns_a_user_with_the_name_when_everything_is_valid(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123'})

        response = self.view(request)

        content = json.loads(response.content)
        self.assertEqual(content['name'], 'Codium')

    def test_should_returns_a_user_with_the_email_when_everything_is_valid(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123'})

        response = self.view(request)

        content = json.loads(response.content)
        self.assertEqual(content['email'], 'info@codium.team')

    def test_should_generate_a_random_id_when_everything_is_valid(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123'})

        response = self.view(request)

        content = json.loads(response.content)
        self.assertIsNotNone(content['id'])

    def test_should_fail_when_password_is_short(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_'})

        response = self.view(request)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Password is not valid')

    def test_should_fail_when_password_does_not_contain_underscore(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass123123'})

        response = self.view(request)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Password is not valid')

    def test_persist_the_user(self) -> None:
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123'})
        self.view(request)

        user = UserFrameworkRepository.get_instance().find_by_email('info@codium.team')
        self.assertIsNotNone(user)

    def test_should_fail_when_email_is_used(self) -> None:
        UserFrameworkRepository.get_instance().save(User(1, 'Codium', 'info@codium.team'))

        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123'})
        response = self.view(request)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'The email is already in use')
