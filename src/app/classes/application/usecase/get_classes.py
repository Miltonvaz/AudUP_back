from src.app.classes.domain.repository import ClassRepository
from src.app.classes.domain.models import CreateClassResponse
from typing import List


class GetClasses():
    def __init__(self, repo : ClassRepository):
        self.repo = repo
    
    
    def execute(self, asignature_id: int)->List[CreateClassResponse]:
        classes = self.repo.get_classes(asignature_id)
        
        return classes
        