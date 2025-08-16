from fastapi import HTTPException
from src.app.transcription.application.use_case.delete_transcription import DeleteTranscription


class DeleteTranscriptionController:
    def __init__(self, usecase: DeleteTranscription):
        self.usecase = usecase

    def execute(self, transcription_id: int):
        try:
            success = self.usecase.execute(transcription_id)
            if not success:
                raise HTTPException(status_code=404, detail="Transcription not found")
            return {"detail": "Transcription deleted successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
