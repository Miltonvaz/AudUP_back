from typing import List
from fastapi import HTTPException
from src.app.user.domain.entities.models import CreateUserResponse
from src.app.user.application.use_case.getAll_user import GetAllUser  

class GetAllUsersController:
    def __init__(self, usecase: GetAllUser):
        self.usecase = usecase

    def execute(self) -> List[CreateUserResponse]:
        try:
            results = self.usecase.execute()
            
            if not results:
                raise HTTPException(status_code=404, detail="No se encontraron usuarios")
            
            return results

        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
