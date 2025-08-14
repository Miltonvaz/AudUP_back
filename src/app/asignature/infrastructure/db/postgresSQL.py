from src.shared.db.database import get_db
from src.app.asignature.domain.repository import AsignatureRepository
from src.shared.db.orm_models import Asignature



class PostgreSQLRepository(AsignatureRepository):
    def __init__(self):
        self.connection = next(get_db())

        if not self.connection:
            print("Hay error")
            return None

    def create(self, asignature: Asignature):

        new_asignature = Asignature(**asignature.dict())

        self.connection.add(new_asignature)

        self.connection.commit()

        self.connection.refresh(new_asignature)

        return new_asignature

    def is_name_taken(self, name: str) -> bool:

        return self.connection.query(Asignature).filter(
            Asignature.name == name
        ).first() is not None

        
