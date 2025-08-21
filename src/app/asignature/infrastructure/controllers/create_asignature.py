from fastapi import HTTPException
from src.app.asignature.domain.models import CreateAsignatureRequest, CreateAsignatureResponse
from src.app.asignature.application.usecase.create_asignature import CreateAsignature
from src.shared.security.auth import Claims

class CreateAsignatureController:
    def __init__(self, useCase: CreateAsignature):
        self.useCase = useCase

    def execute(self, asignature: CreateAsignatureRequest, claims: Claims) -> CreateAsignatureResponse:
        try:
            user_id = claims.user_id

  
            if getattr(claims, "role", None) != "teacher":
                raise HTTPException(status_code=403, detail="Access prohibited. Teachers only.")

            result = self.useCase.execute(asignature, user_id)

            return result

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

