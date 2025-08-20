from src.app.asignature.application.usecase.join_asignature import JoinAsignature
from src.shared.security.auth import Claims
from fastapi import HTTPException


class JoinAsignatureController():
    def __init__(self,  usecase : JoinAsignature):
        self.usecase = usecase
    
    def execute(self, claims : Claims, asignature_id: int)->bool:
        try:
            user_id = claims.user_id
            
            if getattr(claims, "role", None) != "student":
                raise HTTPException(status_code=403, detail="Only students allowed")
            
            return self.usecase.repo.join_asignature(user_id,asignature_id)
        except Exception as e:
            raise e