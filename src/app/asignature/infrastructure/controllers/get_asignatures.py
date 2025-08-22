from src.app.asignature.application.usecase.get_asignatures import GetAsignatures
from src.shared.security.auth import Claims
from fastapi import HTTPException



class GetAsignaturesController():
    def __init__(self, usecase: GetAsignatures):
        self.usecase = usecase
    
    def execute(self, claims: Claims):
        try:
            user_id = claims.user_id
            
            if getattr(claims,"role",None) != "teacher":
                raise HTTPException(status_code=403, detail="Access prohibited. Teachers only.")
            
            return self.usecase.execute(user_id)
            
            
        except Exception as e:
            raise e
