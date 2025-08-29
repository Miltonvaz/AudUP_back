from fastapi import HTTPException, status
from src.app.advertisement.application.usecase.create_advertisement import CreateAdvertisement
from src.app.advertisement.domain.models import CreateAdvertisementRequest, AdvertisementResponse
from src.app.advertisement.domain.repository import AdvertisementRepository
from src.shared.security.auth import Claims


async def create_advertisement_controller(
    request: CreateAdvertisementRequest,
    usecase: CreateAdvertisement,
    repo: AdvertisementRepository,
    claims: Claims = None
) -> AdvertisementResponse:
    """
    Controller para crear un nuevo advertisement
    Solo profesores pueden crear advertisements
    
    Args:
        request: Datos del advertisement a crear
        usecase: Caso de uso para crear advertisement
        repo: Repositorio de advertisements
        claims: Claims del JWT con información del usuario
        
    Returns:
        AdvertisementResponse: Advertisement creado
        
    Raises:
        HTTPException: Si ocurre un error durante la creación
    """
    try:
        # Validar que el usuario es profesor
        if claims and claims.role != "teacher":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only teachers can create advertisements"
            )
        
        # Ejecutar caso de uso
        created_ad = await usecase.execute(request)
        
        # Mapear a response
        return AdvertisementResponse(
            idAdvertisement=created_ad.idAdvertisement,
            idAsignature=created_ad.idAsignature,
            name=created_ad.name,
            description=created_ad.description,
            date=created_ad.date
        )
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating advertisement: {str(e)}"
        )