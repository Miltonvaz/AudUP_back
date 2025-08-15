from fastapi import HTTPException
from src.app.user.domain.entities.models import CreateUserModel, CreateUserResponse
from src.app.user.application.use_case.create_user import CreateUser

class CreateUserController:
    def __init__(self, usecase: CreateUser):
        self.usecase = usecase

    def execute(self, user: CreateUserModel) -> CreateUserResponse:
        try:
            result = self.usecase.execute(user)

            return result  

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
