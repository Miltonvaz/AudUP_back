from datetime import datetime
from sqlalchemy.exc import NoResultFound

from src.shared.db.database import get_db
from src.app.asignature.domain.repository import AsignatureRepository
from src.shared.db.orm_models import Asignature, UserAsignature, User
from src.app.asignature.domain.models import CreateAsignature, UserResponse, TeacherAsignatureResponse
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

    def join_asignature(self, user_id, asignature_id) -> str:
        try:
            existing = (
                self.connection.query(UserAsignature)
                .filter_by(idUser=user_id, idAsignature=asignature_id)
                .first()
            )

            if existing:
                if existing.isActive:
                    return "exists"

                # Reactivar inscripción si estaba desactivada
                existing.isActive = True
                existing.enrolledAt = datetime.now()
                self.connection.commit()
                return "reactivated"

            # Crear nueva inscripción
            new_enrollment = UserAsignature(
                idUser=user_id,
                idAsignature=asignature_id
            )
            self.connection.add(new_enrollment)
            self.connection.commit()
            self.connection.refresh(new_enrollment)

            return "created"

        except Exception as e:
            self.connection.rollback()
            raise e

    def get_students(self, user_id: int, asignature_id: int) -> List[UserResponse]:
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
                    user_id=student.idUser,
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

    def get_asignatures(self, user_id: int) -> List[TeacherAsignatureResponse]:
        try:
            asignatures = (
                self.connection.query(
                    Asignature.idAsignature,
                    Asignature.name,
                    Asignature.description,
                    Asignature.urlBackground,
                    Asignature.linkCode,
                    User.firstName,
                    User.paternalLastName
                )
                .join(User, Asignature.idTeacher == User.idUser)
                .filter(User.idUser == user_id)
                .all()
            )

            return [
                TeacherAsignatureResponse(
                    asignature_id=row.idAsignature,
                    asignatureName=row.name,
                    description=row.description,
                    urlBackground=row.urlBackground,
                    linkCode=row.linkCode,
                    firstName=row.firstName,
                    paternalLastName=row.paternalLastName
                )
                for row in asignatures
            ]

        except Exception as e:
            raise e

    def student_withdraw_from_class(self, user_id: int, asignature_id: int) -> str:
        try:
            existing = (
                self.connection.query(UserAsignature)
                .filter_by(idUser=user_id, idAsignature=asignature_id)
                .first()
            )

            if not existing:
                return "not_found"

            if not existing.isActive:
                return "already_inactive"

            existing.isActive = False
            self.connection.commit()
            return "withdrawn"

        except Exception as e:
            self.connection.rollback()
            raise e

    def teacher_drops_student_from_class(self,asignature_id, student_id) -> str:
        try:
            # Verificar si el estudiante ya ha sido ligado a una clase
            existing = (
                self.connection.query(UserAsignature)
                .filter_by(idUser=student_id, idAsignature=asignature_id)
                .first()
            )

            if not existing:
                return "not_found"

            if not existing.isActive:
                return "already_inactive"
            existing.isActive = False
            self.connection.commit()
            return "withdrawn"

        except Exception as e:
            self.connection.rollback()
            raise e

    def get_student_asignatures(self, user_id: int) -> List[TeacherAsignatureResponse]:
        try:
            asignatures = (
                self.connection.query(
                    Asignature.idAsignature,
                    Asignature.name,
                    Asignature.description,
                    Asignature.urlBackground,
                    Asignature.linkCode,
                    User.firstName,
                    User.paternalLastName
                )
                
                .join(UserAsignature, UserAsignature.idAsignature == Asignature.idAsignature)
                .join(User, Asignature.idTeacher == User.idUser)
                .filter(UserAsignature.idUser == user_id, UserAsignature.isActive == True
                ).all()
            )

            return [
                TeacherAsignatureResponse(
                    asignature_id=row.idAsignature,
                    asignatureName=row.name,
                    description=row.description,
                    urlBackground=row.urlBackground,
                    linkCode=row.linkCode,
                    firstName=row.firstName,               # nombre del maestro
                    paternalLastName=row.paternalLastName  # apellido del maestro
                )
                for row in asignatures
            ]

        except Exception as e:
            raise e
