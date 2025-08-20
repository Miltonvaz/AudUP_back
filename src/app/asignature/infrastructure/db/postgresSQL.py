from datetime import datetime
from sqlalchemy.exc import NoResultFound

from src.shared.db.database import get_db
from src.app.asignature.domain.repository import AsignatureRepository
from src.shared.db.orm_models import Asignature, UserAsignature, User
from src.app.asignature.domain.models import CreateAsignature, UserResponse
from typing import List


class PostgreSQLRepository(AsignatureRepository):
    def __init__(self):
        self.connection = next(get_db())
        if not self.connection:
            raise Exception("No database connection")

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
            return (
                self.connection.query(Asignature)
                .filter(Asignature.name == name)
                .first()
                is not None
            )
        except Exception as e:
            raise e

    def update_background(self, asignature_id: int, background_url: str, user_id: int):
        try:
            asignature = (
                self.connection.query(Asignature)
                .filter(
                    Asignature.idAsignature == asignature_id,
                    Asignature.idTeacher == user_id
                )
                .first()
            )

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
            db_asignature = (
                self.connection.query(Asignature)
                .filter(
                    Asignature.idAsignature == asignature_id,
                    Asignature.idTeacher == user_id
                )
                .first()
            )

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
            return (
                self.connection.query(Asignature)
                .filter(
                    Asignature.idAsignature == asignature_id,
                    Asignature.idTeacher == user_id
                )
                .first()
                is not None
            )
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
            self.connection.rollback()
            raise e

    def join_asignature(self, user_id, asignature_id) -> bool:
        try:
            # Verificar si ya existe una relación
            existing = (
                self.connection.query(UserAsignature)
                .filter_by(idUser=user_id, idAsignature=asignature_id)
                .first()
            )

            if existing:
                if existing.isActive:
                    return False

                # Reactivar inscripción si estaba desactivada
                existing.isActive = True
                existing.enrolledAt = datetime.now()
                self.connection.commit()
                return True

            # Crear nueva inscripción
            new_enrollment = UserAsignature(
                idUser=user_id,
                idAsignature=asignature_id
            )
            self.connection.add(new_enrollment)
            self.connection.commit()
            self.connection.refresh(new_enrollment)

            return True


        except Exception as e:
            self.connection.rollback()
            raise e

    def get_students(self, user_id : int,asignature_id: int) -> List[UserResponse]:
        try:
            # Verificar que la asignatura pertenece al profesor
            asignature = (
                self.connection.query(Asignature)
                .filter_by(idAsignature=asignature_id, idTeacher=user_id)  
                .one()
            )

            # Traer a los estudiantes inscritos en esa asignatura
            students = (
                self.connection.query(User)
                .join(UserAsignature, User.idUser == UserAsignature.idUser)
                .filter(
                    UserAsignature.idAsignature == asignature.idAsignature,
                    UserAsignature.isActive == True
                )
                .all()
            )

            return [
                UserResponse(
                    firstName=student.firstName,
                    secondName=student.secondName,
                    paternalLastName=student.paternalLastName,
                    maternalLastName=student.maternalLastName,
                    email=student.email
                )
                for student in students
            ]

        except NoResultFound:
            raise Exception("This subject does not belong to this teacher")
        except Exception as e:
            raise e