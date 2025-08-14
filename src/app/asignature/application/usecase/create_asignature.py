from src.app.asignature.domain.models import CreateAsignatureModel, CreateResponse
from src.app.asignature.domain.repository import AsignatureRepository


class CreateAsignature():
    def __init__(self, repo: AsignatureRepository):
        self.repo = repo

    def execute(self, asignature: CreateAsignatureModel) -> CreateResponse:
        result = self.repo.create(asignature)

        return CreateResponse(name=result.name, description=result.description)
