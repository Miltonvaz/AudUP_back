from src.app.classes.application.usecase.create_class import CreateClass
from src.shared.security.auth import Claims
from src.app.classes.domain.models import CreateClassRequest
from fastapi import HTTPException
from fastapi.responses import JSONResponse


class CreateClassController():
    def __init__(self, usecase=CreateClass):
        self.usecase = usecase

    def execute(self, claims: Claims, asignature_id: int, class_: CreateClassRequest):

        if getattr(claims, "role", None) != "teacher":
            raise HTTPException(
                status_code=403, detail="Access prohibited. Teachers only.")

        try:
            result = self.usecase.execute(asignature_id, class_)

            if result:
                return JSONResponse(status_code=201, content=result.model_dump(mode="json") )
        except ValueError as ve:
            raise HTTPException(status_code=409, detail=str(ve))
        except Exception as e:
            raise e
