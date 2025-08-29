from fastapi import HTTPException, status
from src.app.advertisement.application.usecase.delete_advertisement import DeleteAdvertisement
from src.app.advertisement.domain.repository import AdvertisementRepository
from src.shared.security.auth import Claims


async def delete_advertisement_controller(
    idAdvertisement: int,
    idAsignature: int,
    usecase: DeleteAdvertisement,
    repo: AdvertisementRepository,
    claims: Claims = None
) -> dict:
    """
    Controller para eliminar un advertisement
    Solo profesores pueden eliminar advertisements de sus asignaturas
    
    Args:
        idAdvertisement: ID del advertisement a eliminar
        idAsignature: ID de la asignatura a la que debe pertenecer
        usecase: Caso de uso para eliminar advertisement
        repo: Repositorio de advertisements
        claims: Claims del JWT con información del usuario
        
    Returns:
        dict: Mensaje de confirmación de eliminación
        
    Raises:
        HTTPException: Si el advertisement no existe, no pertenece a la asignatura o el usuario no tiene permisos
    """
    try:
        # Validar que el usuario es profesor
        if claims and claims.role != "teacher":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only teachers can delete advertisements"
            )

        
        # Ejecutar caso de uso
        deleted = await usecase.execute(idAdvertisement, idAsignature)
        
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Advertisement with ID {idAdvertisement} not found in asignature {idAsignature}"
            )
        
        return {
            "message": f"Advertisement {idAdvertisement} deleted successfully",
            "idAdvertisement": idAdvertisement,
            "idAsignature": idAsignature
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting advertisement: {str(e)}"
        )