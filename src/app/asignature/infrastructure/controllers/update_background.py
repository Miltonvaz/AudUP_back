from src.app.asignature.application.usecase.update_background import UpdateBackground
from fastapi import UploadFile, HTTPException
from src.shared.utils.format_filename import generate_filename
import os
from src.shared.service.drive_service.drive_service import upload_file
from src.shared.security.auth import Claims


class UpdateBackgroundController:
    def __init__(self, usecase: UpdateBackground):
        self.usecase = usecase

    async def execute(self, asignature_id: int, file: UploadFile, claims: Claims):
        try:
            # Validar role del usuario
            user_id = claims.user_id
            if getattr(claims, "role", None) != "teacher":
                raise HTTPException(
                    status_code=403, detail="Access prohibited. Teachers only."
                )

            # Extensiones permitidas
            allowed_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}

            # Obtener extensión
            _, extension = os.path.splitext(file.filename)
            extension = extension.lower()

            # Validar extensión
            if extension not in allowed_extensions:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid file. Only images are allowed: {', '.join(allowed_extensions)}"
                )

            # Formatear nombre
            formatted_name = generate_filename("fondo", extension)
            file.filename = formatted_name

            # Leer el archivo como bytes para pasarlo al UseCase
            file_data = await file.read()
            await file.close()

            # Subir a Google Drive
            url = upload_file(file.filename, file_data, file.content_type)

            # Llamar al UseCase para actualizar URL en la DB
            return await self.usecase.execute(asignature_id, url, user_id)

        except HTTPException:
            raise  # dejar pasar las excepciones que ya definimos
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
