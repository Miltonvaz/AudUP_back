from src.app.asignature.application.usecase.get_students import GetStudents
from typing import List
from src.app.asignature.domain.models import UserResponse
from src.shared.security.auth import Claims
from fastapi import HTTPException
from fastapi.responses import JSONResponse



class GetStudentsController():
    def __init__(self, usecase : GetStudents):
        self.usecase = usecase
    
    def execute(self, claims : Claims, asignature_id : int )->List[UserResponse]:
        
        try:
            user_id = claims.user_id
            
            if getattr(claims, "role", None) != "teacher":
                raise HTTPException(status_code=403, detail="Access prohibited. Teachers only.")
            
            result = self.usecase.execute(user_id,asignature_id)
            if result:
                return JSONResponse(status_code=200, content=[item.dict() for item in result])
        except ValueError as ve:
            raise HTTPException(status_code=404,detail=str(ve))
        except Exception as e:
            raise e
            
            