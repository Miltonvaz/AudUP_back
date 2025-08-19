from fastapi import HTTPException, UploadFile
from typing import Optional
from src.app.user.domain.entities.models import CreateUserModel, CreateUserResponse
from src.app.user.application.use_case.update_user import UpdateUser
from src.shared.service.drive_service import upload_file, generate_filename

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
            if profile_image:
                file_bytes = await profile_image.read()
                extension = profile_image.filename.split(".")[-1]
                filename = generate_filename("profile", extension)
                url = upload_file(filename, file_bytes, profile_image.content_type)
                user_data.urlProfile = url  

            result = self.usecase.execute(user_id, user_data)
            if result is None:
                raise HTTPException(status_code=404, detail="User not found")

            return result

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
