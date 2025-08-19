from fastapi import UploadFile, HTTPException
from src.app.user.domain.entities.models import CreateUserModel, CreateUserResponse
from src.app.user.application.use_case.create_user import CreateUser
from src.shared.service.drive_service.drive_service import upload_file  
from src.shared.utils.format_filename import generate_filename
class CreateUserController:
    def __init__(self, usecase: CreateUser):
        self.usecase = usecase

    async def execute(self, user: CreateUserModel, profile_image: UploadFile = None) -> CreateUserResponse:
        try:
            if profile_image:
                file_bytes = await profile_image.read()
                extension = profile_image.filename.split(".")[-1]
                filename = generate_filename("profile", extension)
                url = upload_file(filename, file_bytes, profile_image.content_type)
                user.urlProfile = url 

            result = self.usecase.execute(user)
            return result  

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
