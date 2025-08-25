from src.app.classes.domain.repository import ClassRepository
from src.app.classes.domain.models import CreateClassResponse
from sqlalchemy.orm.exc import NoResultFound


class GetClass():
    def __init__(self, repo : ClassRepository):
        self.repo = repo 
    
    def execute(self, asignature_id : int, class_id = int)->CreateClassResponse:
        try:
            return self.repo.get_class(asignature_id, class_id)
        except NoResultFound as e:
            # lo relanzamos para que lo atrape el controlador
            raise e