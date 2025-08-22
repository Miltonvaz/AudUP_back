from abc import ABC, abstractmethod
from typing import List, Optional
from src.app.transcription.domain.entities.models import CreateTranscriptionModel

class TranscriptionRepository(ABC):

    @abstractmethod
    def create(self, transcription: CreateTranscriptionModel):
        pass

    @abstractmethod
    def get_by_id(self, transcription_id: int) -> Optional[CreateTranscriptionModel]:
        pass

    @abstractmethod
    def get_all(self) -> List[CreateTranscriptionModel]:
        pass

    @abstractmethod
    def update(self, transcription_id: int, transcription: CreateTranscriptionModel) -> bool:
        pass

    @abstractmethod
    def delete(self, transcription_id: int) -> bool:
        pass