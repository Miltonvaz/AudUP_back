from src.app.classes.domain.models import CreateClassRequest
from src.app.classes.domain.repository import ClassRepository


class EditClass():
    def __init__(self, repo = ClassRepository ):
        self.repo = repo
        
    def execute(self,asignature_id : int, class_id : int,class_ : CreateClassRequest)->None:
        
        if self.repo.existing_class(asignature_id,class_):
            raise ValueError("The class name already exists")
        
        self.repo.edit_class(asignature_id,class_id,class_)