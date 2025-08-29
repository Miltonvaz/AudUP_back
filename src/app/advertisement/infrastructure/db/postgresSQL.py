from datetime import datetime
from sqlalchemy.exc import NoResultFound
from typing import List

from src.shared.db.database import get_db
from src.app.advertisement.domain.repository import AdvertisementRepository
from src.shared.db.orm_models import Advertisement as ORMAdvertisement, Asignature
from src.app.advertisement.domain.models import Advertisement


class PostgreSQLRepository(AdvertisementRepository):
    def __init__(self):
        self.connection = next(get_db())
        if not self.connection:
            raise Exception("No database connection")

    async def create(self, advertisement: Advertisement) -> Advertisement:
        """Crea un nuevo advertisement y retorna el advertisement creado con su ID"""
        try:
            # Verificar que la asignatura existe
            asignature = (
                self.connection.query(Asignature)
                .filter(Asignature.idAsignature == advertisement.idAsignature)
                .first()
            )
            
            if not asignature:
                raise Exception(f"Asignature with ID {advertisement.idAsignature} not found")

            new_advertisement = ORMAdvertisement(
                idAsignature=advertisement.idAsignature,
                name=advertisement.name,
                description=advertisement.description
                # date se asigna automáticamente por el server_default
            )

            self.connection.add(new_advertisement)
            self.connection.commit()
            self.connection.refresh(new_advertisement)

            return Advertisement(
                idAdvertisement=new_advertisement.idAdvertisement,
                idAsignature=new_advertisement.idAsignature,
                name=new_advertisement.name,
                description=new_advertisement.description,
                date=new_advertisement.date
            )

        except Exception as e:
            self.connection.rollback()
            raise e

    async def get_all_by_asignature(self, idAsignature: int) -> List[Advertisement]:
        """Obtiene todos los advertisements de una asignatura específica"""
        try:
            # Verificar que la asignatura existe
            asignature = (
                self.connection.query(Asignature)
                .filter(Asignature.idAsignature == idAsignature)
                .first()
            )
            
            if not asignature:
                raise Exception(f"Asignature with ID {idAsignature} not found")

            advertisements = (
                self.connection.query(ORMAdvertisement)
                .filter(ORMAdvertisement.idAsignature == idAsignature)
                .order_by(ORMAdvertisement.date.desc())  # Ordenar por fecha descendente
                .all()
            )

            return [
                Advertisement(
                    idAdvertisement=ad.idAdvertisement,
                    idAsignature=ad.idAsignature,
                    name=ad.name,
                    description=ad.description,
                    date=ad.date
                )
                for ad in advertisements
            ]

        except Exception as e:
            raise e

    async def get_by_id(self, idAdvertisement: int) -> Advertisement | None:
        """Obtiene un advertisement por su ID, retorna None si no existe"""
        try:
            advertisement = (
                self.connection.query(ORMAdvertisement)
                .filter(ORMAdvertisement.idAdvertisement == idAdvertisement)
                .first()
            )

            if not advertisement:
                return None

            return Advertisement(
                idAdvertisement=advertisement.idAdvertisement,
                idAsignature=advertisement.idAsignature,
                name=advertisement.name,
                description=advertisement.description,
                date=advertisement.date
            )

        except Exception as e:
            raise e

    async def update(self, idAdvertisement: int, data: dict) -> Advertisement:
        """Actualiza un advertisement y retorna el advertisement actualizado"""
        try:
            advertisement = (
                self.connection.query(ORMAdvertisement)
                .filter(ORMAdvertisement.idAdvertisement == idAdvertisement)
                .first()
            )

            if not advertisement:
                raise Exception(f"Advertisement with ID {idAdvertisement} not found")

            # Actualizar solo los campos proporcionados
            for key, value in data.items():
                if hasattr(advertisement, key):
                    setattr(advertisement, key, value)

            self.connection.commit()
            self.connection.refresh(advertisement)

            return Advertisement(
                idAdvertisement=advertisement.idAdvertisement,
                idAsignature=advertisement.idAsignature,
                name=advertisement.name,
                description=advertisement.description,
                date=advertisement.date
            )

        except Exception as e:
            self.connection.rollback()
            raise e

    async def delete(self, idAdvertisement: int) -> None:
        """Elimina un advertisement por su ID"""
        try:
            advertisement = (
                self.connection.query(ORMAdvertisement)
                .filter(ORMAdvertisement.idAdvertisement == idAdvertisement)
                .first()
            )

            if not advertisement:
                raise Exception(f"Advertisement with ID {idAdvertisement} not found")

            self.connection.delete(advertisement)
            self.connection.commit()

        except Exception as e:
            self.connection.rollback()
            raise e

    def exists_advertisement_in_asignature(self, idAdvertisement: int, idAsignature: int) -> bool:
        """Verifica si un advertisement existe y pertenece a una asignatura específica"""
        try:
            return (
                self.connection.query(ORMAdvertisement)
                .filter(
                    ORMAdvertisement.idAdvertisement == idAdvertisement,
                    ORMAdvertisement.idAsignature == idAsignature
                )
                .first()
                is not None
            )
        except Exception as e:
            raise e

    def is_name_taken_in_asignature(self, idAsignature: int, name: str, exclude_id: int = None) -> bool:
        """Verifica si ya existe un advertisement con el mismo nombre en la asignatura"""
        try:
            query = (
                self.connection.query(ORMAdvertisement)
                .filter(
                    ORMAdvertisement.idAsignature == idAsignature,
                    ORMAdvertisement.name == name
                )
            )
            
            # Excluir el advertisement actual en caso de actualización
            if exclude_id:
                query = query.filter(ORMAdvertisement.idAdvertisement != exclude_id)
            
            return query.first() is not None
            
        except Exception as e:
            raise e