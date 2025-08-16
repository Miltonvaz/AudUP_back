from fastapi import HTTPException
from typing import Optional
from src.app.transcription.domain.entities.models import TranscriptionResponse
from src.app.transcription.application.use_case.getById_transcription import GetTranscriptionById

class GetTranscriptionByIdController:
    def __init__(self, usecase: GetTranscriptionById):
        self.usecase = usecase

    def execute(self, user_id: int) -> Optional[TranscriptionResponse]:
        try:
            result = self.usecase.execute(user_id)
            if result is None:
                raise HTTPException(status_code=404, detail="Transcription not found")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
