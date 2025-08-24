from abc import abstractmethod, ABC
from src.app.classes.domain.models import CreateClassRequest, CreateClassResponse


class ClassRepository(ABC):
    
    @abstractmethod
    def create(self, asignature_id : int,class_ : CreateClassRequest)->CreateClassResponse:
        pass
    @abstractmethod
    def existing_class(self, asignature_id: int, class_ : CreateClassResponse )-> bool:
        pass
