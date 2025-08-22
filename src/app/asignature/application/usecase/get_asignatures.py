from src.app.asignature.domain.models import TeacherAsignatureResponse
from src.app.asignature.domain.repository import AsignatureRepository
from typing import List

class GetAsignatures():
    def __init__(self, repo : AsignatureRepository):
        self.repo = repo
    
    def execute(self, user_id : int)->List[TeacherAsignatureResponse]:
        return self.repo.get_asignatures(user_id)

    
            
    
        