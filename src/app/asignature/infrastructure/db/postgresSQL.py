from src.shared.db.database import get_db
from src.app.asignature.domain.repository import AsignatureRepository
from src.shared.db.orm_models import Asignature
from src.app.asignature.domain.models import CreateAsignature


class PostgreSQLRepository(AsignatureRepository):
    def __init__(self):
        self.connection = next(get_db())

        if not self.connection:
            return None

    def create(self, asignature: CreateAsignature, user_id: int):
        try:
            new_asignature = Asignature(
                name=asignature.name,
                description=asignature.description,
                idTeacher=user_id
            )

            self.connection.add(new_asignature)
            self.connection.commit()
            self.connection.refresh(new_asignature)

            return new_asignature

        except Exception as e:
            self.connection.rollback()
            raise e

    def is_name_taken(self, name: str) -> bool:
        try:
            return self.connection.query(Asignature).filter(
                Asignature.name == name
            ).first() is not None
        except Exception as e:
            raise e

    def update_background(self, asignature_id: int, background_url: str, user_id: int):
        try:
            asignature = self.connection.query(Asignature).filter(
                Asignature.idAsignature == asignature_id,
                Asignature.idTeacher == user_id
            ).first()

            if not asignature:
                raise Exception("Subject not found or without permissions")

            asignature.urlBackground = background_url
            self.connection.commit()
            self.connection.refresh(asignature)
            return asignature

        except Exception as e:
            self.connection.rollback()
            raise e

    def update(self, asignature: CreateAsignature, user_id: int, asignature_id: int):
        try:
            db_asignature = self.connection.query(Asignature).filter(
                Asignature.idAsignature == asignature_id,
                Asignature.idTeacher == user_id
            ).first()

            if not db_asignature:
                raise Exception("Subject not found or without permissions")

            for key, value in asignature.dict().items():
                setattr(db_asignature, key, value)

            self.connection.commit()
            self.connection.refresh(db_asignature)
            return db_asignature

        except Exception as e:
            self.connection.rollback()
            raise e

    def exists_asignature(self, user_id, asignature_id) -> bool:
        try:
            return self.connection.query(Asignature).filter(
                Asignature.idAsignature == asignature_id,
                Asignature.idTeacher == user_id
            ).first() is not None
        except Exception as e:
            raise e

    def delete(self, user_id, asignature_id) -> bool:
        try:
            asignature = (
                self.connection.query(Asignature)
                .filter(
                    Asignature.idTeacher == user_id,
                    Asignature.idAsignature == asignature_id
                )
                .first()
            )
            
            if not asignature:
                return False
        
            self.connection.delete(asignature)
            self.connection.commit()
            return True
        
        except Exception as e:
            raise e
