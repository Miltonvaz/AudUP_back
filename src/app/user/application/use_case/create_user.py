from datetime import datetime
from src.app.user.domain.entities.models import CreateUserModel, CreateUserResponse
from src.app.user.domain.repository import UserRepository
from src.shared.security.hash import hash_password

class CreateUser:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, user: CreateUserModel) -> CreateUserResponse:
        user.passwordHash = hash_password(user.passwordHash)

        result = self.repo.create(user)

        return CreateUserResponse(
            idUser=result.idUser,
            idRol=result.idRol,
            firstName=result.firstName,
            secondName=result.secondName,
            paternalLastName=result.paternalLastName,
            maternalLastName=result.maternalLastName,
            email=result.email,
            urlProfile=result.urlProfile,
            createdAt=str(result.createdAt) if result.createdAt else datetime.utcnow().isoformat()
        )
