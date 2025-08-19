from abc import ABC, abstractmethod
from src.app.asignature.domain.models import CreateAsignatureRequest, CreateAsignatureResponse


class AsignatureRepository(ABC):
    @abstractmethod
    def create(self, asignature: CreateAsignatureRequest, user_id: int) -> CreateAsignatureResponse:
        pass

    @abstractmethod
    def is_name_taken(self, name: str) -> bool:
        pass

    @abstractmethod
    def update_background(self, asignature_id: int, background_url: str, user_id: int):
        pass

    @abstractmethod
    def update(self, asignature: CreateAsignatureRequest, user_id: int, asignature_id: int) -> CreateAsignatureResponse:
        pass
