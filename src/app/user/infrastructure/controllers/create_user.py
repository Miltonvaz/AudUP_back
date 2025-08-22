from fastapi import UploadFile, HTTPException
from pydantic import EmailStr, ValidationError
from src.app.user.domain.entities.models import CreateUserModel, CreateUserResponse
from src.app.user.application.use_case.create_user import CreateUser
from src.shared.service.drive_service.drive_service import upload_file  
from src.shared.utils.format_filename import generate_filename

ALLOWED_FILE_TYPES = {"image/jpeg", "image/png", "image/webp"}

class CreateUserController:
    def __init__(self, usecase: CreateUser):
        self.usecase = usecase

    async def execute(self, user: CreateUserModel, profile_image: UploadFile = None) -> CreateUserResponse:
        try:
            if not user.name or not user.email:
                raise HTTPException(status_code=400, detail="Nombre y email son obligatorios")

            try:
                EmailStr.validate(user.email)
            except Exception:
                raise HTTPException(status_code=422, detail="Formato de email inválido")

            if profile_image:
                if profile_image.content_type not in ALLOWED_FILE_TYPES:
                    raise HTTPException(
                        status_code=415,
                        detail="Tipo de archivo no soportado (solo JPG, PNG, WEBP)"
                    )

                file_bytes = await profile_image.read()
                extension = profile_image.filename.split(".")[-1].lower()
                filename = generate_filename("profile", extension)

                try:
                    url = upload_file(filename, file_bytes, profile_image.content_type)
                    user.urlProfile = url
                except Exception as e:
                    raise HTTPException(status_code=500, detail=f"Error subiendo archivo: {str(e)}")

            try:
                result = self.usecase.execute(user)
                return result
            except ValueError as ve:
                raise HTTPException(status_code=400, detail=str(ve))
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

        except ValidationError as ve:
            raise HTTPException(status_code=422, detail=ve.errors())
        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")
