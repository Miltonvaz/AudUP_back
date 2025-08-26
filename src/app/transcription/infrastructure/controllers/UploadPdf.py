from fastapi import HTTPException, UploadFile
from src.shared.service.drive_service.drive_service import upload_file
from src.shared.utils.format_filename import generate_filename
from src.shared.security.auth import Claims
from src.app.transcription.application.use_case.update_transcription import UpdateTranscription
from src.app.transcription.domain.entities.models import CreateTranscriptionModel

ALLOWED_FILE_TYPES = ["application/pdf"]

class UploadPdfController:
    def __init__(self, usecase: UpdateTranscription):
        self.usecase = usecase

    async def execute(self, transcription_id: int, pdf_file: UploadFile, claims: Claims) -> str:
        try:
            if getattr(claims, "role", None) != "teacher":
                raise HTTPException(status_code=403, detail="Access prohibited. Teachers only.")

            if not pdf_file:
                raise HTTPException(status_code=400, detail="No se envió ningún archivo")

            if pdf_file.content_type not in ALLOWED_FILE_TYPES:
                raise HTTPException(status_code=415, detail="Tipo de archivo no soportado (solo PDF)")

            file_bytes = await pdf_file.read()
            await pdf_file.close()

            if not file_bytes:
                raise HTTPException(status_code=400, detail="El archivo está vacío")

            extension = pdf_file.filename.split(".")[-1]
            filename = generate_filename("transcription", extension)

            url = upload_file(filename, file_bytes, pdf_file.content_type)

            transcription_update = CreateTranscriptionModel(
                idClass=0,
                title="",
                content="",
                urlFile=url
            )

            updated_transcription = self.usecase.execute(transcription_id, transcription_update)

            if not updated_transcription:
                raise HTTPException(status_code=404, detail="Transcripción no encontrada")

            return url

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
