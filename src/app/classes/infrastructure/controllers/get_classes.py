from src.app.classes.application.usecase.get_classes import GetClasses
from src.shared.security.auth import Claims
from fastapi import HTTPException
from sqlalchemy.orm.exc import NoResultFound



class GetClassesController():
    def __init__(self, usecase : GetClasses):
        self.usecase = usecase
        
    def execute(self, claims: Claims, asignature_id: int):
        
        if getattr(claims, "role",None) not in ["teacher", "student"]:
            raise HTTPException(status_code=403, detail="Access prohibited")
        
        try:
                return self.usecase.execute(asignature_id)
        except NoResultFound as nf:
            raise HTTPException(status_code=404, detail=str(nf))
        except Exception as e:
            raise e