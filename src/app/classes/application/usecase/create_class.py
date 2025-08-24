from src.app.classes.domain.repository import ClassRepository
from src.app.classes.domain.models import CreateClassRequest, CreateClassResponse

class CreateClass():
    def __init__(self, repo : ClassRepository):
        self.repo = repo
    
    def execute(self, asignature_id : int, class_: CreateClassRequest)-> CreateClassResponse:
        if self.repo.existing_class(asignature_id, class_):
            raise ValueError("The class name already exists")
        
        result = self.repo.create(asignature_id,class_)
        
        return CreateClassResponse(
            class_id = result.class_id,
            name     = result.name,
            date     = result.date
        )