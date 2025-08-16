from src.app.transcription.domain.repository import TranscriptionRepository


class DeleteTranscription():
    def __init__(self, repo: TranscriptionRepository):
        self.repo = repo

    def execute(self, user_id: int) -> bool:
        return self.repo.delete(user_id)
