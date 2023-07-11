import smtplib
import ssl
from random import randint

from django.http import JsonResponse, HttpResponseBadRequest, HttpRequest, HttpResponse
from src.domain.user import User
from src.infrastructure.user_framework_repository import UserFrameworkRepository


class RegisterUser:
    def __init__(self, user_repository: UserFrameworkRepository) -> None:
        self.user_repository = user_repository

    def execute(self, request: HttpRequest) -> HttpResponse:
        if len(request.POST['password']) <= 8:
            return HttpResponseBadRequest('Password is not valid')
        if "_" not in request.POST['password']:
            return HttpResponseBadRequest('Password is not valid')
        if self.user_repository.find_by_email(request.POST['email']) is not None:
            return HttpResponseBadRequest('The email is already in use')

        user = User(randint(1, 999999), request.POST['name'], request.POST['email'])
        self.user_repository.save(user)

        # Send a confirmation email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context):
            pass
            # Uncomment this lines with a valid username and password
            # server.login("my@gmail.com", "myPassword")
            # server.sendmail('info@codium.team', request.POST['email'], 'Confirmation link')

        return JsonResponse({'name': user.name, 'email': user.email, 'id': user.user_id})
