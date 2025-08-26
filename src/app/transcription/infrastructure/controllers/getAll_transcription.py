from typing import List
from fastapi import HTTPException
from src.app.transcription.domain.entities.models import TranscriptionResponse
from src.app.transcription.application.use_case.getAll_transcription import GetAllTranscription

class GetAllTranscriptionController:
    def __init__(self, usecase: GetAllTranscription):
        self.usecase = usecase

    def execute(self, user_role: str) -> List[TranscriptionResponse]:
        try:
            if not user_role:
                raise HTTPException(status_code=400, detail="Rol de usuario no proporcionado")
            if not isinstance(user_role, str):
                raise HTTPException(status_code=422, detail="Rol de usuario inválido")
            if user_role.lower() != "teacher":
                raise HTTPException(status_code=403, detail="Solo los profesores pueden acceder a las transcripciones")

            results = self.usecase.execute()
            if results is None:
                raise HTTPException(status_code=404, detail="No se encontraron transcripciones")

            if not isinstance(results, list):
                raise HTTPException(status_code=500, detail="Formato de datos inesperado")

            return results

        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
