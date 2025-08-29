from fastapi import HTTPException, status
from src.app.advertisement.application.usecase.get_advertisement_by_id import GetAdvertisementById
from src.app.advertisement.domain.models import AdvertisementResponse
from src.app.advertisement.domain.repository import AdvertisementRepository
from src.shared.security.auth import Claims


async def get_advertisement_by_id_controller(
    idAdvertisement: int,
    idAsignature: int,
    usecase: GetAdvertisementById,
    repo: AdvertisementRepository,
    claims: Claims = None
) -> AdvertisementResponse:
    """
    Controller para obtener un advertisement específico por ID
    Tanto profesores como estudiantes pueden ver advertisements (con las validaciones correspondientes)
    
    Args:
        idAdvertisement: ID del advertisement a buscar
        idAsignature: ID de la asignatura a la que debe pertenecer
        usecase: Caso de uso para obtener advertisement por ID
        repo: Repositorio de advertisements
        claims: Claims del JWT con información del usuario
        
    Returns:
        AdvertisementResponse: Advertisement encontrado
        
    Raises:
        HTTPException: Si el advertisement no existe o no pertenece a la asignatura
    """
    try:
        
        # Ejecutar caso de uso
        ad = await usecase.execute(idAdvertisement, idAsignature)
        
        if not ad:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Advertisement with ID {idAdvertisement} not found in asignature {idAsignature}"
            )
        
        # Mapear a response
        return AdvertisementResponse(
            idAdvertisement=ad.idAdvertisement,
            idAsignature=ad.idAsignature,
            name=ad.name,
            description=ad.description,
            date=ad.date
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching advertisement: {str(e)}"
        )