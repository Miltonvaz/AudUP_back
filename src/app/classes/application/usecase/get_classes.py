from src.app.classes.domain.repository import ClassRepository
from src.app.classes.domain.models import CreateClassResponse
from typing import List
from sqlalchemy.orm.exc import NoResultFound


class GetClasses():
    def __init__(self, repo : ClassRepository):
        self.repo = repo
    
    
    def execute(self, asignature_id: int)->List[CreateClassResponse]:
        try:
            return self.repo.get_classes(asignature_id)
        except NoResultFound as e:
            # lo relanzamos para que lo atrape el controlador
            raise e