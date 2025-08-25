from src.app.asignature.application.usecase.get_student_asignatures import GetStudentAsignatures
from src.shared.security.auth import Claims
from fastapi.responses import JSONResponse
from fastapi import HTTPException


class GetStudentAsignaturesController():
    def __init__(self, usecase : GetStudentAsignatures):
        self.usecase = usecase
        
    def execute(self, claims: Claims):
        try:
            user_id = claims.user_id
            
            if getattr(claims,"role",None) != "student":
                raise HTTPException(status_code=403, detail="Access prohibited. Students only.")
            
            result = self.usecase.execute(user_id)
            
            if result:
                return JSONResponse(status_code=200, content=[item.dict() for item in result])
            
            
        except Exception as e:
            raise e
