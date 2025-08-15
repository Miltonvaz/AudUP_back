from typing import Optional
from src.app.user.domain.repository import UserRepository
from src.shared.security.hash import check_password
from src.shared.security.auth import generate_jwt

class LoginUser:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, email: str, password: str) -> Optional[dict]:
        # Buscar usuario por email
        user = self.repo.get_by_email(email)
        if user is None:
            return None

        # Validar hash de contraseña
        try:
            if not user.passwordHash:
                return None
            if not check_password(user.passwordHash, password):
                return None
        except Exception:
            # Si bcrypt falla por hash inválido, lo tratamos como credenciales inválidas
            return None

        # Generar token JWT
        token = generate_jwt(user.idUser, user.email, user.idRol)

        return {
            "idUser": user.idUser,
            "idRol": user.idRol,
            "token": token
        }
