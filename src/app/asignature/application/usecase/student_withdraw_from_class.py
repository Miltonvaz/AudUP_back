from src.app.asignature.domain.repository import AsignatureRepository

class StudentWithdrawFromClass:
    def __init__(self, repo: AsignatureRepository):
        self.repo = repo
    
    def execute(self, user_id: int, asignature_id: int) -> str:
        result = self.repo.student_withdraw_from_class(user_id, asignature_id)

        if result == "not_found":
            raise ValueError("Student is not enrolled in this class.")
        elif result == "already_inactive":
            raise ValueError("Student is already inactive in this class.")
        elif result == "error":
            raise ValueError("Unexpected error occurred while withdrawing student.")

        return "withdrawn"
