from fastapi import HTTPException, status
from src.app.advertisement.application.usecase.update_advertisement import UpdateAdvertisement
from src.app.advertisement.domain.models import UpdateAdvertisementRequest, AdvertisementResponse
from src.app.advertisement.domain.repository import AdvertisementRepository
from src.shared.security.auth import Claims


async def update_advertisement_controller(
    idAdvertisement: int,
    idAsignature: int,
    request: UpdateAdvertisementRequest,
    usecase: UpdateAdvertisement,
    repo: AdvertisementRepository,
    claims: Claims = None
) -> AdvertisementResponse:
    """
    Controller para actualizar un advertisement existente
    Solo profesores pueden actualizar advertisements
    
    Args:
        idAdvertisement: ID del advertisement a actualizar
        idAsignature: ID de la asignatura a la que debe pertenecer
        request: Datos de actualización
        usecase: Caso de uso para actualizar advertisement
        repo: Repositorio de advertisements
        claims: Claims del JWT con información del usuario
        
    Returns:
        AdvertisementResponse: Advertisement actualizado
        
    Raises:
        HTTPException: Si el advertisement no existe, no pertenece a la asignatura,
                      el usuario no es profesor, o hay error de validación
    """
    try:
        # Validar que el usuario es profesor
        if claims and claims.role != "teacher":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only teachers can update advertisements"
            )
        
        # Ejecutar caso de uso
        updated_ad = await usecase.execute(idAdvertisement, idAsignature, request)
        
        if not updated_ad:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Advertisement with ID {idAdvertisement} not found in asignature {idAsignature}"
            )
        
        # Mapear a response
        return AdvertisementResponse(
            idAdvertisement=updated_ad.idAdvertisement,
            idAsignature=updated_ad.idAsignature,
            name=updated_ad.name,
            description=updated_ad.description,
            date=updated_ad.date
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
            detail=f"Error updating advertisement: {str(e)}"
        )