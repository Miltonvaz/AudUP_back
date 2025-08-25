from src.app.classes.application.usecase.get_class import GetClass
from src.shared.security.auth import Claims
from fastapi import HTTPException
from sqlalchemy.orm.exc import NoResultFound


class GetClassController():
    def __init__(self, usecase : GetClass):
        self.usecase = usecase
    
    
    
    def execute(self, claims : Claims, asignature_id : int, class_id : int):
        
        if getattr(claims, "role",None) not in ["teacher", "student"]:
            raise HTTPException(status_code=403, detail="Access prohibited")

        try:
                return self.usecase.execute(asignature_id, class_id)
        except NoResultFound as nf:
            raise HTTPException(status_code=404, detail=str(nf))
        
        except Exception as e:
            raise e