from fastapi import HTTPException
from typing import Optional
from src.app.user.domain.entities.models import CreateUserResponse
from src.app.user.application.use_case.getByEmail import GetUserByEmail

class GetUserByEmailController:
    def __init__(self, usecase: GetUserByEmail):
        self.usecase = usecase

    def execute(self, email: str) -> Optional[CreateUserResponse]:
        try:
            result = self.usecase.execute(email)
            if result is None:
                raise HTTPException(status_code=404, detail="User not found")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
