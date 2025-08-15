from typing import Optional
from src.app.user.domain.entities.models import CreateUserModel, CreateUserResponse
from src.app.user.domain.repository import UserRepository
from src.shared.security.hash import hash_password


class UpdateUser:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, user_id: int, user_data: CreateUserModel) -> Optional[CreateUserResponse]:

        if user_data.passwordHash:
            user_data.passwordHash = hash_password(user_data.passwordHash)

        updated_user = self.repo.update(user_id, user_data)
        if updated_user is None:
            return None

        return CreateUserResponse(
            idUser=updated_user.idUser,
            idRol=updated_user.idRol,
            firstName=updated_user.firstName,
            secondName=updated_user.secondName,
            paternalLastName=updated_user.paternalLastName,
            maternalLastName=updated_user.maternalLastName,
            email=updated_user.email,
            createdAt=updated_user.created_at.isoformat()  
        )
