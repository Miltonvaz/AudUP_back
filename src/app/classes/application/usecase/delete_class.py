from src.app.classes.domain.repository import ClassRepository


class DeleteClass():
    def __init__(self, repo : ClassRepository):
        self.repo = repo
    
    def execute(self, asignature_id: int,class_id : int)->bool:
        result  = self.repo.delete(asignature_id,class_id)
        
        if result == False:
            raise ValueError("Class not found")
        
        return result