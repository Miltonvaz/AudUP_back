from typing import Optional
from src.app.transcription.domain.entities.models import TranscriptionResponse
from src.app.transcription.domain.repository import TranscriptionRepository


class GetTranscriptionById:
    def __init__(self, repo: TranscriptionRepository):
        self.repo = repo

    def execute(self, transcription_id: int) -> Optional[TranscriptionResponse]:
        result = self.repo.get_by_id(transcription_id)

        if result is None:
            return None

        return TranscriptionResponse(
            idTranscription=result.idTranscription,
            idClass=result.idClass,
            title=result.title,
            content=result.content
        )
