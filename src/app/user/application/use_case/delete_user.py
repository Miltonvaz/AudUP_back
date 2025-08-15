from src.app.user.domain.repository import UserRepository


class DeleteUser():
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, user_id: int) -> bool:
        return self.repo.delete(user_id)
