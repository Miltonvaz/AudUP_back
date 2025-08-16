from datetime import datetime
from src.app.transcription.domain.entities.models import CreateTranscriptionModel, TranscriptionResponse
from src.app.transcription.domain.repository import TranscriptionRepository


class CreateTranscription:
    def __init__(self, repo: TranscriptionRepository):
        self.repo = repo

    def execute(self, transcription: CreateTranscriptionModel) -> TranscriptionResponse:
        result = self.repo.create(transcription)

        return TranscriptionResponse(
            idTranscription=result.idTranscription,
            idClass=result.idClass,
            title=result.title,
            content=result.content
        )
