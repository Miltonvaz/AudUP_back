from src.app.asignature.domain.repository import AsignatureRepository

class JoinAsignature:
    def __init__(self, repo: AsignatureRepository):
        self.repo = repo
        
    def execute(self, user_id: int, asignature_id: int) -> None:
        if not self.repo.exists_asignature(user_id, asignature_id):
            raise ValueError("Asignature not found")
        
        success = self.repo.join_asignature(user_id, asignature_id)
        if not success:
            raise ValueError("Could not join asignature")
