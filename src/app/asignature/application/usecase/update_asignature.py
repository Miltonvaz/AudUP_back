from src.app.asignature.domain.repository import AsignatureRepository
from src.app.asignature.domain.models import CreateAsignatureRequest, CreateAsignatureResponse


class UpdateAsignature():
    def __init__(self, repo: AsignatureRepository):
        self.repo = repo

    def execute(self, asignature: CreateAsignatureRequest, user_id: int, asignature_id: int) -> CreateAsignatureResponse:
        result = self.repo.update(asignature, user_id, asignature_id)

        return CreateAsignatureResponse(name=result.name, description=result.description)
