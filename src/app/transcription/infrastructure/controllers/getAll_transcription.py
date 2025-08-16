from typing import List
from src.app.transcription.domain.entities.models import TranscriptionResponse
from src.app.transcription.application.use_case.getAll_transcription import GetAllTranscription  

class GetAllTranscriptionController:
    def __init__(self, usecase: GetAllTranscription):
        self.usecase = usecase

    def execute(self) -> List[TranscriptionResponse]:
        results = self.usecase.execute()  
     
        return results
