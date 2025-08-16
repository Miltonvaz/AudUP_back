from typing import Optional
from src.app.transcription.domain.entities.models import CreateTranscriptionModel, TranscriptionResponse
from src.app.transcription.domain.repository import TranscriptionRepository


class UpdateTranscription:
    def __init__(self, repo: TranscriptionRepository):
        self.repo = repo

    def execute(self, transcription_id: int, transcription_data: CreateTranscriptionModel) -> Optional[TranscriptionResponse]:
        updated_transcription = self.repo.update(transcription_id, transcription_data)
        if updated_transcription is None:
            return None

        return TranscriptionResponse(
            idTranscription=updated_transcription.idTranscription,
            idClass=updated_transcription.idClass,
            title=updated_transcription.title,
            content=updated_transcription.content
        )
