from fastapi import HTTPException
from src.app.transcription.domain.entities.models import CreateTranscriptionModel, TranscriptionResponse
from src.app.transcription.application.use_case.create_transcription import CreateTranscription

class CreateTranscriptionController:
    def __init__(self, usecase: CreateTranscription):
        self.usecase = usecase

    def execute(self, transcription: CreateTranscriptionModel) -> TranscriptionResponse:
        try:
            result = self.usecase.execute(transcription)

            return result  

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
