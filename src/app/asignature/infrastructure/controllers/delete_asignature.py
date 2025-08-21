from src.app.asignature.application.usecase.delete_asignature import DeleteAsignature
from src.shared.security.auth import Claims
from fastapi import HTTPException
from fastapi.responses import JSONResponse

class DeleteAsignatureController:
    def __init__(self, usecase: DeleteAsignature):
        self.usecase = usecase

    def execute(self, claims: Claims, asignature_id: int):
        user_id = claims.user_id
        
        # Validar rol
        if getattr(claims, "role", None) != "teacher":
            raise HTTPException(
                status_code=403, detail="Access prohibited. Teachers only."
            )

        try:
            if self.usecase.execute(user_id, asignature_id):
                return JSONResponse(status_code=200, content={"detail: ": "Asignature deleted successfully"})
        except ValueError as ve:
            raise HTTPException(status_code=404, detail=str(ve))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        
