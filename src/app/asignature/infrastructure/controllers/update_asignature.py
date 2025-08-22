from src.app.asignature.application.usecase.update_asignature import UpdateAsignature
from src.app.asignature.domain.models import CreateAsignatureRequest, CreateAsignatureResponse
from src.shared.security.auth import Claims
from fastapi import HTTPException
from fastapi.responses import JSONResponse

class UpdateAsignatureController():
    def __init__(self, usecase: UpdateAsignature):
        self.usecase = usecase
    
    def execute(self,asignature_id : int,asignature: CreateAsignatureRequest,claims: Claims)-> CreateAsignatureResponse:
        try:
            user_id = claims.user_id
            
            if getattr(claims, "role", None) != "teacher":
                raise HTTPException(status_code=403, detail="Access prohibited. Teachers only.")
            
            result = self.usecase.execute(asignature,user_id,asignature_id)
            
            if result:
                return JSONResponse(status_code=200,content=result.dict())
    
        except ValueError as ve:
            raise HTTPException(status_code=400, detail= str(ve))
        except HTTPException as e:
            raise e
            

            
            