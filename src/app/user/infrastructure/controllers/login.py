from fastapi import HTTPException
from src.app.user.application.use_case.login import LoginUser

class LoginUserController:
    def __init__(self, usecase: LoginUser):
        self.usecase = usecase

    def execute(self, email: str, password: str) -> dict:
        try:
            if not email or not password:
                raise HTTPException(status_code=400, detail="Email y contraseña son obligatorios")

            result = self.usecase.execute(email, password)
            if result is None:
                raise HTTPException(status_code=401, detail="Email o contraseña inválidos")

            return result

        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
