from src.shared.db.database import get_db
from src.app.classes.domain.repository import ClassRepository
from src.app.classes.domain.models import CreateClassRequest, CreateClassResponse
from src.shared.db.orm_models import Class
from datetime import datetime

class PosgreSQLRepository(ClassRepository):
    def __init__(self):
        self.connection = next(get_db())
        if not self.connection:
            raise Exception("No database connection")

    def create(self, asignature_id : int, new_class: CreateClassRequest) -> CreateClassResponse:
        try:

            class_ = Class(
                name=new_class.name,
                idAsignature=asignature_id
            )

            self.connection.add(class_)
            self.connection.commit()
            self.connection.refresh(class_)

            response = CreateClassResponse(
                class_id=class_.idClass,
                name=class_.name,
                date=class_.date
            )

            return response
        except Exception as e:
            raise e

    def existing_class(self, asignature_id: int, class_: CreateClassRequest) -> bool:
        try:
            return(
                self.connection.query(Class).filter(
                Class.idAsignature == asignature_id,
                Class.name == class_.name
            ).first() is not None
            )

            
        except Exception as e:
            raise e
    
    def edit_class(self, asignature_id: int, class_id : int,class_:CreateClassRequest)-> None:
        try:
            db_class = self.connection.query(Class).filter(
                Class.idAsignature == asignature_id,
                Class.idClass == class_id
            ).first()
            
            if not db_class:
                raise Exception("Not found")
            
            db_class.name = class_.name
            db_class.date = datetime.now()
            self.connection.commit()
        
        except Exception as e:
            raise e
        
