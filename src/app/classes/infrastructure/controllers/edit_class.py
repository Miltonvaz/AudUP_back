from src.app.classes.application.usecase.edit_class import EditClass
from src.shared.security.auth import Claims
from src.app.classes.domain.models import CreateClassRequest
from fastapi import HTTPException, status, Response


class EditClassController():
    def __init__(self, usecase : EditClass):
        self.usecase = usecase
    
    def execute(self, claims: Claims, asignature_id: int, class_id : int,class_: CreateClassRequest):
        if getattr(claims, "role", None) != "teacher":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access prohibited. Teachers only."
            )

        try:
            self.usecase.execute(asignature_id,class_id, class_)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unexpected error while editing class"
            )

      
        return Response(status_code=status.HTTP_204_NO_CONTENT)