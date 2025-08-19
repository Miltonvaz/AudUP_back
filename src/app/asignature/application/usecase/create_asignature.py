from src.app.asignature.domain.models import CreateAsignatureRequest, CreateAsignatureResponse
from src.app.asignature.domain.repository import AsignatureRepository


class CreateAsignature():
    def __init__(self, repo: AsignatureRepository):
        self.repo = repo

    def execute(self, asignature: CreateAsignatureRequest, user_id : int) -> CreateAsignatureResponse:
        result = self.repo.create(asignature, user_id)

        return CreateAsignatureResponse(name=result.name, description=result.description)
