from fastapi import HTTPException
from typing import Optional
from src.app.user.domain.entities.models import CreateUserResponse
from src.app.user.application.use_case.getById_user import GetUserById

class GetUserByIdController:
    def __init__(self, usecase: GetUserById):
        self.usecase = usecase

    def execute(self, user_id: int) -> Optional[CreateUserResponse]:
        try:
            result = self.usecase.execute(user_id)
            if result is None:
                raise HTTPException(status_code=404, detail="User not found")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
