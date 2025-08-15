from typing import Optional
from src.app.user.domain.entities.models import CreateUserResponse
from src.app.user.domain.repository import UserRepository


class GetUserById:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, user_id: int) -> Optional[CreateUserResponse]:
        result = self.repo.get_by_id(user_id)

        if result is None:
            return None

        return CreateUserResponse(
            idUser=result.idUser,
            idRol=result.idRol,
            firstName=result.firstName,
            secondName=result.secondName,
            paternalLastName=result.paternalLastName,
            maternalLastName=result.maternalLastName,
            email=result.email,
            createdAt=result.created_at.isoformat()  
        )
