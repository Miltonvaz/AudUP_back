from typing import List
from src.app.user.domain.entities.models import CreateUserResponse
from src.app.user.domain.repository import UserRepository

class GetAllUser:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self) -> List[CreateUserResponse]:
        users = self.repo.get_all()
        return [
            CreateUserResponse(
                idUser=user.idUser,
                idRol=user.idRol,
                firstName=user.firstName,
                secondName=user.secondName,
                paternalLastName=user.paternalLastName,
                maternalLastName=user.maternalLastName,
                email=user.email,
                createdAt=user.created_at.isoformat()  
            )
            for user in users
        ]
