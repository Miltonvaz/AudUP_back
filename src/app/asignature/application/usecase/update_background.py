from src.app.asignature.domain.repository import AsignatureRepository

class UpdateBackground:
    def __init__(self, repo: AsignatureRepository):
        self.repo = repo

    async def execute(self, asignature_id: int, background_url: str, user_id: int):
        updated_asignature = self.repo.update_background(asignature_id, background_url, user_id)

        
        return {
            "name": updated_asignature.name,
            "background_url": updated_asignature.urlBackground
        }
