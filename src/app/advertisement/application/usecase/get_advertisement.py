from typing import List
from src.app.advertisement.domain.models import Advertisement
from src.app.advertisement.domain.repository import AdvertisementRepository


class GetAdvertisements:
    def __init__(self, repo: AdvertisementRepository):
        self.repo = repo

    async def execute(self, idAsignature: int) -> List[Advertisement]:
        """
        Obtiene todos los advertisements de una asignatura específica
        Los advertisements solo existen dentro del contexto de una asignatura
        
        Args:
            idAsignature: ID de la asignatura
            
        Returns:
            Lista de advertisements de la asignatura
        """
        ads = await self.repo.get_all_by_asignature(idAsignature)
        return ads