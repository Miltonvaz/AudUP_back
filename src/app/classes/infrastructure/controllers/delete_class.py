from src.app.classes.application.usecase.delete_class import DeleteClass
from src.shared.security.auth import Claims
from fastapi import HTTPException
from fastapi.responses import JSONResponse


class DeleteClassController():
    def __init__(self, usecase: DeleteClass):
        self.usecase = usecase

    def execute(self, claims: Claims, asignature_id: int, class_id: int):

        if getattr(claims, "role", None) != "teacher":
            raise HTTPException(
                status_code=403, detail="Access prohibited. Teachers only.")

        try:
            result = self.usecase.execute(asignature_id, class_id)

            if result == True:
                return JSONResponse(status_code=200, content={"Message": "Class successfully deleted"})

        except ValueError as ve:
            raise HTTPException(status_code=404, detail=str(ve))

        except Exception as e:
            raise e
