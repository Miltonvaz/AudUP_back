from src.app.classes.domain.repository import ClassRepository
from src.app.classes.domain.models import CreateClassResponse


class GetClass():
    def __init__(self, repo : ClassRepository):
        self.repo = repo 
    
    def execute(self, asignature_id : int, class_id = int)->CreateClassResponse:
        class_ = self.repo.get_class(asignature_id, class_id)
        
        return class_
    