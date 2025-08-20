from src.app.asignature.domain.repository import AsignatureRepository
from src.app.asignature.domain.models import UserResponse
from typing import List



class GetStudents():
    def __init__(self, repo : AsignatureRepository):
        self.repo = repo
    
    def execute(self, user_id: int,asignature_id: int)->List[UserResponse]:
        if not self.repo.exists_asignature(user_id,asignature_id):
            raise ValueError("Asignature not found")
        
        return self.repo.get_students(user_id,asignature_id)
        