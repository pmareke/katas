from django.http import JsonResponse, HttpResponseBadRequest, HttpRequest, HttpResponse
from django.views import View

from src.domain.exceptions import EmailAlreadyInUseException, InvalidPasswordException
from src.infrastructure.user_framework_repository import UserFrameworkRepository
from src.use_cases.register_user import RegisterUser

class UserController(View):
    user_repository = UserFrameworkRepository()
    register_user = RegisterUser(user_repository)

    def __init__(self, register_user: RegisterUser) -> None:
        self.register_user = register_user
        super().__init__()

    def get(self) -> HttpResponse:
        return JsonResponse("Hello, world. You're at the polls index.")

    def post(self, request: HttpRequest) -> HttpResponse:
        try:
            name = request.POST["name"]
            password = request.POST["password"]
            email = request.POST["email"]
            user = self.register_user.execute(name, password, email)
            return JsonResponse(user)
        except InvalidPasswordException:
            return HttpResponseBadRequest('Password is not valid')
        except EmailAlreadyInUseException:
            return HttpResponseBadRequest('The email is already in use')
