from fastapi import HTTPException
from src.app.user.application.use_case.delete_user import DeleteUser

class DeleteUserController:
    def __init__(self, usecase: DeleteUser):
        self.usecase = usecase

    def execute(self, user_id: int):
        try:
            success = self.usecase.execute(user_id)
            if not success:
                raise HTTPException(status_code=404, detail="User not found")
            return {"detail": "User deleted successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
