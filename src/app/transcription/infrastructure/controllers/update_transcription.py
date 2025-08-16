from fastapi import HTTPException
from typing import Optional
from src.app.transcription.domain.entities.models import CreateTranscriptionModel, TranscriptionResponse
from src.app.transcription.application.use_case.update_transcription import UpdateTranscription

class UpdateTranscriptionController:
    def __init__(self, usecase: UpdateTranscription):
        self.usecase = usecase

    def execute(self, transcription_id: int, transcription_data: CreateTranscriptionModel) -> Optional[TranscriptionResponse]:
        try:
            result = self.usecase.execute(transcription_id, transcription_data)
            if result is None:
                raise HTTPException(status_code=404, detail="Transcription not found")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
