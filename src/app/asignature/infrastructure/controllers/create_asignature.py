from fastapi import HTTPException
from src.app.asignature.domain.models import CreateAsignatureModel, CreateResponse
from src.app.asignature.application.usecase.create_asignature import CreateAsignature
from src.shared.security.auth import Claims

class CreateAsignatureController:
    def __init__(self, useCase: CreateAsignature):
        self.useCase = useCase

    def execute(self, asignature: CreateAsignatureModel, claims: Claims) -> CreateResponse:
        try:
            user_id = claims.user_id

  
            if getattr(claims, "role", None) != "teacher":
                raise HTTPException(status_code=403, detail="Acceso no permitido. Solo teachers.")

            result = self.useCase.execute(asignature, user_id)

            return result

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
