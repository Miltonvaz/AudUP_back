# getAll.py - Controller corregido
from typing import List
from src.app.user.domain.entities.models import CreateUserResponse
from src.app.user.application.use_case.getAll_user import GetAllUser  # <-- Use Case

class GetAllUsersController:
    def __init__(self, usecase: GetAllUser):
        self.usecase = usecase

    def execute(self) -> List[CreateUserResponse]:
        results = self.usecase.execute()  
     
        return results
