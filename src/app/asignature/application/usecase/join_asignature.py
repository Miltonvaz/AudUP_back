from src.app.asignature.domain.repository import AsignatureRepository

class JoinAsignature:
    def __init__(self, repo: AsignatureRepository):
        self.repo = repo
        
    def execute(self, user_id: int, asignature_id: int) -> str:
        
        result = self.repo.join_asignature(user_id, asignature_id)
        
        if not result:
            raise ValueError("Could not join asignature")
        
        return result