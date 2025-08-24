from src.app.classes.application.usecase.get_classes import GetClasses
from src.shared.security.auth import Claims
from fastapi import HTTPException



class GetClassesController():
    def __init__(self, usecase : GetClasses):
        self.usecase = usecase
        
    def execute(self, claims: Claims, asignature_id: int):
        
        if getattr(claims, "role",None) != "teacher":
            raise HTTPException(status_code=403, detail="Access prohibited. Teachers only.")
        
        try:
                return self.usecase.execute(asignature_id)
        
        except Exception as e:
            raise e