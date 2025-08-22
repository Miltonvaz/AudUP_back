from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.shared.security.auth import Claims
from src.app.asignature.application.usecase.student_withdraw_from_class import StudentWithdrawFromClass

class StudentWithdrawFromClassController:
    def __init__(self, usecase: StudentWithdrawFromClass):
        self.usecase = usecase
    
    def execute(self, claims: Claims, asignature_id: int):
        user_id = claims.user_id

        if getattr(claims, "role", None) != "student":
            raise HTTPException(status_code=403, detail="Only students can withdraw")

        try:
            result = self.usecase.execute(user_id, asignature_id)
            if result == "withdrawn":
                return JSONResponse(status_code=200, content={"message": "Student withdrawn successfully."})
        
        except ValueError as ve:
            detail = str(ve)
            if "not enrolled" in detail:
                raise HTTPException(status_code=404, detail=detail)
            elif "inactive" in detail:
                raise HTTPException(status_code=400, detail=detail)
            else:
                raise HTTPException(status_code=500, detail=detail)
