from typing import Optional
from src.app.advertisement.domain.models import Advertisement
from src.app.advertisement.domain.repository import AdvertisementRepository

class GetAdvertisementById:
    def __init__(self, repo: AdvertisementRepository):
        self.repo = repo

    async def execute(self, idAdvertisement: int, idAsignature: int) -> Optional[Advertisement]:
        """
        Obtiene un advertisement específico por su ID dentro de una asignatura
        Valida que el advertisement pertenezca a la asignatura especificada
        
        Args:
            idAdvertisement: ID del advertisement a buscar
            idAsignature: ID de la asignatura a la que debe pertenecer
            
        Returns:
            Advertisement encontrado o None si no existe o no pertenece a la asignatura
        """
        ad = await self.repo.get_by_id(idAdvertisement)
        
        # Verificar que el advertisement existe y pertenece a la asignatura correcta
        if ad and ad.idAsignature == idAsignature:
            return ad
        
        return None