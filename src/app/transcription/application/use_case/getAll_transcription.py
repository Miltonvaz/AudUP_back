from typing import List
from src.app.transcription.domain.entities.models import TranscriptionResponse
from src.app.transcription.domain.repository import TranscriptionRepository


class GetAllTranscription:
    def __init__(self, repo: TranscriptionRepository):
        self.repo = repo

    def execute(self) -> List[TranscriptionResponse]:
        transcriptions = self.repo.get_all()
        return [
            TranscriptionResponse(
                idTranscription=transcription.idTranscription,
                idClass=transcription.idClass,
                title=transcription.title,
                content=transcription.content
            )
            for transcription in transcriptions
        ]
