from typing import Optional
from src.app.user.domain.entities.models import CreateUserResponse
from src.app.user.domain.repository import UserRepository

class GetUserByEmail:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, email: str) -> Optional[CreateUserResponse]:
        user = self.repo.get_by_email(email)
        if user is None:
            return None

        return CreateUserResponse(
            idUser=user.idUser,
            idRol=user.idRol,
            firstName=user.firstName,
            secondName=user.secondName,
            paternalLastName=user.paternalLastName,
            maternalLastName=user.maternalLastName,
            email=user.email,
            createdAt=user.created_at.isoformat()  
        )
