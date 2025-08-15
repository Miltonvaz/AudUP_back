from abc import ABC, abstractmethod
from src.app.asignature.domain.models import CreateAsignatureModel

class AsignatureRepository(ABC):
    @abstractmethod
    def create(self, asignature: CreateAsignatureModel, user_id: int):
        pass
    def is_name_taken(self, name: str) ->bool:
        pass