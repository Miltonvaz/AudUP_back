from fastapi import HTTPException
from src.app.transcription.domain.entities.models import CreateTranscriptionModel, TranscriptionResponse
from src.app.transcription.application.use_case.create_transcription import CreateTranscription
from pydantic import ValidationError

class CreateTranscriptionController:
    def __init__(self, usecase: CreateTranscription):
        self.usecase = usecase

    def execute(self, transcription: CreateTranscriptionModel, user_role: str) -> TranscriptionResponse:
        try:
            if user_role != "teacher":
                raise HTTPException(status_code=403, detail="Solo los profesores pueden crear transcripciones")

            if not transcription or not transcription.content:
                raise HTTPException(status_code=400, detail="El contenido de la transcripción es obligatorio")

            result = self.usecase.execute(transcription)

            if result is None:
                raise HTTPException(status_code=500, detail="No se pudo crear la transcripción")

            return result

        except ValidationError as ve:
            raise HTTPException(status_code=422, detail=ve.errors())

        except HTTPException as he:
            raise he

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
