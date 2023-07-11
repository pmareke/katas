from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views import View
from src.infrastructure.user_framework_repository import UserFrameworkRepository
from src.use_cases.register_user import RegisterUser

class UserController(View):
    user_repository: UserFrameworkRepository | None = None

    def __init__(self, user_repository: UserFrameworkRepository) -> None:
        super().__init__()
        self.user_repository = user_repository

    def get(self) -> HttpResponse:
        return JsonResponse("Hello, world. You're at the polls index.")

    def post(self, request: HttpRequest) -> HttpResponse:
        assert self.user_repository

        register_user = RegisterUser(self.user_repository)
        return register_user.execute(request)
