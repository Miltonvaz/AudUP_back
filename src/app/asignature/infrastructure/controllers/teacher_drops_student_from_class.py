from src.app.asignature.application.usecase.teacher_drops_student_from_class import TeacherDropsStudentFromClass
from src.shared.security.auth import Claims
from fastapi import HTTPException
from fastapi.responses import JSONResponse


class TeacherDropsStudentFromClassController():
    def __init__(self, usecase : TeacherDropsStudentFromClass):
        self.usecase = usecase
    
    def execute(self, claims: Claims, asignature_id, student_id):
       
        teacher_id = claims.user_id
            
        if getattr(claims,"role",None) != "teacher":
            raise HTTPException(status_code=403, detail="Access prohibited. Teachers only.")
        
        try:
            result = self.usecase.execute(student_id, asignature_id)
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
            
            
            
                