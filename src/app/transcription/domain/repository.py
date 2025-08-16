from abc import ABC, abstractmethod
from typing import List, Optional
from src.app.transcription.domain.entities.models import CreateTranscriptionModel


class TranscriptionRepository(ABC):

    @abstractmethod
    def create(self, user: CreateTranscriptionModel):
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[CreateTranscriptionModel]:
        pass

    @abstractmethod
    def get_all(self) -> List[CreateTranscriptionModel]:
        pass

    @abstractmethod
    def update(self, user_id: int, user: CreateTranscriptionModel) -> bool:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass

