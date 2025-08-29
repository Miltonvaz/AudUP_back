from domain.repository import AdvertisementRepository


class DeleteAdvertisement:
    def __init__(self, repo: AdvertisementRepository):
        self.repo = repo

    async def execute(self, idAdvertisement: int, idAsignature: int) -> bool:
        """
        Elimina un advertisement por su ID dentro de una asignatura específica
        Valida que el advertisement pertenezca a la asignatura antes de eliminarlo
        
        Args:
            idAdvertisement: ID del advertisement a eliminar
            idAsignature: ID de la asignatura a la que debe pertenecer
            
        Returns:
            True si se eliminó correctamente, False si no existía o no pertenece a la asignatura
        """
        # Verificar que el advertisement existe y pertenece a la asignatura correcta
        existing_ad = await self.repo.get_by_id(idAdvertisement)
        if not existing_ad or existing_ad.idAsignature != idAsignature:
            return False
        
        # Eliminar el advertisement
        await self.repo.delete(idAdvertisement)
        return True