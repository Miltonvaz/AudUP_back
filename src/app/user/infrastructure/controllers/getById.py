from fastapi import HTTPException
from typing import Optional
from src.app.user.domain.entities.models import CreateUserResponse
from src.app.user.application.use_case.getById_user import GetUserById

class GetUserByIdController:
    def __init__(self, usecase: GetUserById):
        self.usecase = usecase

    def execute(self, user_id: int) -> Optional[CreateUserResponse]:
        try:
            if not isinstance(user_id, int) or user_id <= 0:
                raise HTTPException(status_code=400, detail="ID de usuario inválido")

            result = self.usecase.execute(user_id)
            if result is None:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            return result

        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
