from typing import Optional
from domain.models import Advertisement, UpdateAdvertisementRequest
from domain.repository import AdvertisementRepository


class UpdateAdvertisement:
    def __init__(self, repo: AdvertisementRepository):
        self.repo = repo

    async def execute(
        self, 
        idAdvertisement: int,
        idAsignature: int,
        request: UpdateAdvertisementRequest
    ) -> Optional[Advertisement]:
        """
        Actualiza un advertisement existente dentro de una asignatura específica
        
        Args:
            idAdvertisement: ID del advertisement a actualizar
            idAsignature: ID de la asignatura a la que debe pertenecer
            request: Datos de actualización
            
        Returns:
            Advertisement actualizado o None si no existe o no pertenece a la asignatura
            
        Raises:
            ValueError: Si no se proporciona ningún campo para actualizar
        """
        # Verificar que el advertisement existe y pertenece a la asignatura
        existing_ad = await self.repo.get_by_id(idAdvertisement)
        if not existing_ad or existing_ad.idAsignature != idAsignature:
            return None
        
        # Preparar datos para actualización (solo campos no None)
        update_data = {}
        if request.name is not None:
            update_data['name'] = request.name
        if request.description is not None:
            update_data['description'] = request.description
            
        # Verificar que hay al menos un campo para actualizar
        if not update_data:
            raise ValueError("At least one field must be provided for update")
        
        # Realizar actualización
        updated_ad = await self.repo.update(idAdvertisement, update_data)
        return updated_ad