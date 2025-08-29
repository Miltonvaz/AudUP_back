from src.app.advertisement.domain.models import Advertisement, CreateAdvertisementRequest
from src.app.advertisement.domain.repository import AdvertisementRepository


class CreateAdvertisement:
    def __init__(self, repo: AdvertisementRepository):
        self.repo = repo

    async def execute(self, request: CreateAdvertisementRequest) -> Advertisement:
        """
        Crea un nuevo advertisement basado en la solicitud
        
        Args:
            request: Datos para crear el advertisement
            
        Returns:
            Advertisement creado con su ID asignado
        """
        # Crear el modelo de dominio desde el request
        ad = Advertisement(
            idAdvertisement=None,  # Se asignará en la BD
            idAsignature=request.idAsignature,
            name=request.name,
            description=request.description,
            date=None  # Se asignará en la BD
        )
        
        # Crear en el repositorio
        created_ad = await self.repo.create(ad)
        return created_ad