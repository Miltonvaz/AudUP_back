from fastapi import HTTPException
from typing import Optional
from src.app.user.domain.entities.models import CreateUserModel, CreateUserResponse
from src.app.user.application.use_case.update_user import UpdateUser

class UpdateUserController:
    def __init__(self, usecase: UpdateUser):
        self.usecase = usecase

    def execute(self, user_id: int, user_data: CreateUserModel) -> Optional[CreateUserResponse]:
        try:
            result = self.usecase.execute(user_id, user_data)
            if result is None:
                raise HTTPException(status_code=404, detail="User not found")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
