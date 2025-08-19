from src.app.asignature.domain.repository import AsignatureRepository

class DeleteAsignature():
    def __init__(self, repo : AsignatureRepository):
        self.repo = repo
        
    def execute(self, user_id: int, asignature_id : int)->bool:
        
        if not self.repo.exists_asignature(user_id,asignature_id):
            raise ValueError("Asignature not found")
        
        return self.repo.delete(user_id,asignature_id)
        
        
        