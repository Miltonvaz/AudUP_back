from fastapi import HTTPException
from typing import Optional
from src.app.transcription.domain.entities.models import TranscriptionResponse
from src.app.transcription.application.use_case.getById_transcription import GetTranscriptionById

class GetTranscriptionByIdController:
    def __init__(self, usecase: GetTranscriptionById):
        self.usecase = usecase

    def execute(self, transcription_id: int, user_role: str) -> Optional[TranscriptionResponse]:
        try:
            if not isinstance(transcription_id, int) or transcription_id <= 0:
                raise HTTPException(status_code=400, detail="ID de transcripción inválido")

            if not user_role:
                raise HTTPException(status_code=400, detail="Rol de usuario no proporcionado")
            if not isinstance(user_role, str):
                raise HTTPException(status_code=422, detail="Rol de usuario inválido")
            if user_role.lower() != "teacher":
                raise HTTPException(status_code=403, detail="Solo los profesores pueden acceder a la transcripción")

            result = self.usecase.execute(transcription_id)
            if result is None:
                raise HTTPException(status_code=404, detail="Transcripción no encontrada")
            if not isinstance(result, TranscriptionResponse):
                raise HTTPException(status_code=500, detail="Formato de datos inesperado")

            return result

        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
