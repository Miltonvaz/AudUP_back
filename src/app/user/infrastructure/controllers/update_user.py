from fastapi import HTTPException, UploadFile
from typing import Optional
from src.app.user.domain.entities.models import CreateUserModel, CreateUserResponse
from src.app.user.application.use_case.update_user import UpdateUser
from src.shared.service.drive_service.drive_service import upload_file
from src.shared.utils.format_filename import generate_filename

ALLOWED_FILE_TYPES = {"image/jpeg", "image/png", "image/webp"}

class UpdateUserController:
    def __init__(self, usecase: UpdateUser):
        self.usecase = usecase

    async def execute(
        self,
        user_id: int,
        user_data: CreateUserModel,
        profile_image: UploadFile = None
    ) -> Optional[CreateUserResponse]:
        try:
            if not isinstance(user_id, int) or user_id <= 0:
                raise HTTPException(status_code=400, detail="ID de usuario inválido")

    
            if profile_image:
                if profile_image.content_type not in ALLOWED_FILE_TYPES:
                    raise HTTPException(
                        status_code=415,
                        detail="Tipo de archivo no soportado (solo JPG, PNG, WEBP)"
                    )

                file_bytes = await profile_image.read()
                if not file_bytes:
                    raise HTTPException(status_code=400, detail="El archivo está vacío")

                extension = profile_image.filename.split(".")[-1].lower()
                filename = generate_filename("profile", extension)

                try:
                    url = upload_file(filename, file_bytes, profile_image.content_type)
                    user_data.urlProfile = url
                except Exception as e:
                    raise HTTPException(status_code=500, detail=f"Error subiendo archivo: {str(e)}")

            result = self.usecase.execute(user_id, user_data)
            if result is None:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            return result

        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
