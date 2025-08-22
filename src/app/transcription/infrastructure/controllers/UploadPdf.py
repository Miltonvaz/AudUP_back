from fastapi import HTTPException, UploadFile
from src.shared.service.drive_service.drive_service import upload_file
from src.shared.utils.format_filename import generate_filename
from src.shared.security.auth import Claims

ALLOWED_FILE_TYPES = ["application/pdf"]

class UploadPdfController:
    def __init__(self):
        pass

    async def execute(self, pdf_file: UploadFile, claims: Claims) -> str:
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

            try:
                url = upload_file(filename, file_bytes, pdf_file.content_type)
                return url
            except Exception as e:
                raise HTTPException(status_code=502, detail=f"Error al subir el archivo: {str(e)}")

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
