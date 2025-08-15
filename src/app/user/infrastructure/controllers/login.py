from fastapi import HTTPException
from typing import Optional
from src.app.user.application.use_case.login import LoginUser

class LoginUserController:
    def __init__(self, usecase: LoginUser):
        self.usecase = usecase

    def execute(self, email: str, password: str) -> dict:
        try:
            result = self.usecase.execute(email, password)
            if result is None:
                # Credenciales inválidas
                raise HTTPException(
                    status_code=401,
                    detail="Invalid email or password"
                )
            return result

        except HTTPException:
            # Si ya es un HTTPException, la dejamos pasar
            raise

        except Exception as e:
            # Cualquier otro error no controlado
            raise HTTPException(
                status_code=500,
                detail="Internal server error"
            )
