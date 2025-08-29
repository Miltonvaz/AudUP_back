from abc import ABC, abstractmethod
from typing import List
from .models import Advertisement


class AdvertisementRepository(ABC):
    @abstractmethod
    async def create(self, advertisement: Advertisement) -> Advertisement:
        """Crea un nuevo advertisement y retorna el advertisement creado con su ID"""
        ...

    @abstractmethod
    async def get_all_by_asignature(self, idAsignature: int) -> List[Advertisement]:
        """Obtiene todos los advertisements de una asignatura específica"""
        ...

    @abstractmethod
    async def get_by_id(self, idAdvertisement: int) -> Advertisement | None:
        """Obtiene un advertisement por su ID, retorna None si no existe"""
        ...

    @abstractmethod
    async def update(self, idAdvertisement: int, data: dict) -> Advertisement:
        """Actualiza un advertisement y retorna el advertisement actualizado"""
        ...

    @abstractmethod
    async def delete(self, idAdvertisement: int) -> None:
        """Elimina un advertisement por su ID"""
        ...