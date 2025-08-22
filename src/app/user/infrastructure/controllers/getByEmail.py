from fastapi import HTTPException
from typing import Optional
from src.app.user.domain.entities.models import CreateUserResponse
from src.app.user.application.use_case.getByEmail import GetUserByEmail

class GetUserByEmailController:
    def __init__(self, usecase: GetUserByEmail):
        self.usecase = usecase

    def execute(self, email: str) -> Optional[CreateUserResponse]:
        try:
            if not email:
                raise HTTPException(status_code=400, detail="El email es obligatorio")

            result = self.usecase.execute(email)
            if result is None:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            return result

        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
