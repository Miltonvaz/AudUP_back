from fastapi import HTTPException, status
from typing import List
from src.app.advertisement.application.usecase.get_advertisements import GetAdvertisements
from src.app.advertisement.domain.models import AdvertisementResponse
from src.app.advertisement.domain.repository import AdvertisementRepository
from src.shared.security.auth import Claims


async def get_advertisements_controller(
    idAsignature: int,
    usecase: GetAdvertisements,
    repo: AdvertisementRepository,
    claims: Claims = None
) -> List[AdvertisementResponse]:
    """
    Controller para obtener todos los advertisements de una asignatura
    Tanto profesores como estudiantes pueden ver advertisements
    
    Args:
        idAsignature: ID de la asignatura
        usecase: Caso de uso para obtener advertisements
        repo: Repositorio de advertisements
        claims: Claims del JWT con información del usuario
        
    Returns:
        List[AdvertisementResponse]: Lista de advertisements de la asignatura
        
    Raises:
        HTTPException: Si ocurre un error durante la consulta
    """
    try:
        
        # Ejecutar caso de uso
        ads = await usecase.execute(idAsignature)
        
        # Mapear a response
        return [
            AdvertisementResponse(
                idAdvertisement=ad.idAdvertisement,
                idAsignature=ad.idAsignature,
                name=ad.name,
                description=ad.description,
                date=ad.date
            )
            for ad in ads
        ]
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching advertisements: {str(e)}"
        )