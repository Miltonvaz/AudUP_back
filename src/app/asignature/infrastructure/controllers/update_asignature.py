from src.app.asignature.application.usecase.update_asignature import UpdateAsignature
from src.app.asignature.domain.models import CreateAsignatureRequest, CreateAsignatureResponse
from src.shared.security.auth import Claims
from fastapi import HTTPException

class UpdateAsignatureController():
    def __init__(self, usecase: UpdateAsignature):
        self.usecase = usecase
    
    def execute(self,asignature_id : int,asignature: CreateAsignatureRequest,claims: Claims)-> CreateAsignatureResponse:
        try:
            user_id = claims.user_id
            
            if getattr(claims, "role", None) != "teacher":
                raise HTTPException(status_code=403, detail="Access prohibited. Teachers only.")
            
            return self.usecase.repo.update(asignature,user_id,asignature_id)
    
        except HTTPException:
            raise  # dejar pasar las excepciones que ya definimos
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
            
            

            
            