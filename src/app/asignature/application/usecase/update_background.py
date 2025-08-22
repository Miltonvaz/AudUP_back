from src.app.asignature.domain.repository import AsignatureRepository


class UpdateBackground:
    def __init__(self, repo: AsignatureRepository):
        self.repo = repo

    async def execute(self, asignature_id: int, background_url: str, user_id: int):
        if not self.repo.exists_asignature(user_id, asignature_id):
            raise ValueError("Asignature not found")

        updated_asignature = self.repo.update_background(
            asignature_id, background_url, user_id)

        return {
            "name": updated_asignature.name,
            "background_url": updated_asignature.urlBackground
        }
