from fastapi import HTTPException
from src.app.transcription.application.use_case.delete_transcription import DeleteTranscription

class DeleteTranscriptionController:
    def __init__(self, usecase: DeleteTranscription):
        self.usecase = usecase

    def execute(self, transcription_id: int, user_role: str):
        try:
            if user_role != "teacher":
                raise HTTPException(status_code=403, detail="Solo los profesores pueden eliminar transcripciones")

            if not isinstance(transcription_id, int) or transcription_id <= 0:
                raise HTTPException(status_code=400, detail="ID de transcripción inválido")

            success = self.usecase.execute(transcription_id)
            if not success:
                raise HTTPException(status_code=404, detail="Transcripción no encontrada")

            return {"detail": "Transcripción eliminada exitosamente"}

        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
