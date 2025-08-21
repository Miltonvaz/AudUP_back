from src.app.asignature.application.usecase.get_students import GetStudents
from typing import List
from src.app.asignature.domain.models import UserResponse
from src.shared.security.auth import Claims
from fastapi import HTTPException



class GetStudentsController():
    def __init__(self, usecase : GetStudents):
        self.usecase = usecase
    
    def execute(self, claims : Claims, asignature_id : int )->List[UserResponse]:
        
        try:
            user_id = claims.user_id
            
            if getattr(claims, "role", None) != "teacher":
                raise HTTPException(status_code=403, detail="Access prohibited. Teachers only.")
            
            return self.usecase.execute(user_id,asignature_id)
        
        except Exception as e:
            raise e
            
            