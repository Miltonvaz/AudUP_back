from typing import List, Optional
from fastapi import HTTPException, status
from src.shared.db.database import get_db
from src.app.transcription.domain.repository import TranscriptionRepository
from src.app.transcription.domain.entities.models import CreateTranscriptionModel
from src.shared.db.orm_models import Transcription
from sqlalchemy.exc import IntegrityError


class PostgreSQLTranscriptionRepository(TranscriptionRepository):
    def __init__(self):
        self.connection = next(get_db())
        if not self.connection:
            print("Error al obtener la conexión")
            return None

    def create(self, transcription: CreateTranscriptionModel) -> Transcription:
        new_transcription = Transcription(**transcription.dict())
        try:
            self.connection.add(new_transcription)
            self.connection.commit()
            self.connection.refresh(new_transcription)
            return new_transcription
        except Exception:
            self.connection.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error"
            )

    def get_by_id(self, transcription_id: int) -> Optional[Transcription]:
        return self.connection.query(Transcription).filter(Transcription.idTranscription == transcription_id).first()

    def get_all(self) -> List[Transcription]:
        return self.connection.query(Transcription).all()

    def update(self, transcription_id: int, transcription: CreateTranscriptionModel) -> Optional[Transcription]:
        existing_transcription = self.connection.query(Transcription).filter(
            Transcription.idTranscription == transcription_id
        ).first()
        if not existing_transcription:
            return None
        try:
            for key, value in transcription.dict(exclude_unset=True).items():
                setattr(existing_transcription, key, value)
            self.connection.commit()
            self.connection.refresh(existing_transcription)
            return existing_transcription
        except Exception:
            self.connection.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error"
            )

    def delete(self, transcription_id: int) -> bool:
        transcription = self.connection.query(Transcription).filter(Transcription.idTranscription == transcription_id).first()
        if not transcription:
            return False
        try:
            self.connection.delete(transcription)
            self.connection.commit()
            return True
        except Exception:
            self.connection.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error"
            )
