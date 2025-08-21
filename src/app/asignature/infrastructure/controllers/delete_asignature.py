from src.app.asignature.application.usecase.delete_asignature import DeleteAsignature
from src.shared.security.auth import Claims
from fastapi import HTTPException

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
            deleted = self.usecase.execute(user_id, asignature_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        if not deleted:
            raise HTTPException(
                status_code=404, detail="Asignature not found"
            )

        return {"message": f"Asignature deleted successfully"}
