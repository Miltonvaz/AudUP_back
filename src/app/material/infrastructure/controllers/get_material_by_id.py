from fastapi import HTTPException, status
from src.app.material.application.usecase.get_material_by_id import GetMaterialById
from src.app.material.domain.models import MaterialResponse
from src.app.material.domain.repository import MaterialRepository
from src.shared.security.auth import Claims


async def get_material_by_id_controller(
    material_id: int,
    class_id: int,
    usecase: GetMaterialById,
    repo: MaterialRepository,
    claims: Claims = None
) -> MaterialResponse:
    """
    Controller para obtener un material por su ID dentro de una clase.
    
    Args:
        material_id: ID del material
        class_id: ID de la clase a la que pertenece el material
        usecase: Caso de uso para obtener material
        repo: Repositorio de material
        claims: Claims del JWT con información del usuario
        
    Returns:
        MaterialResponse: Material encontrado
        
    Raises:
        HTTPException: Si no existe o usuario no tiene permisos
    """
    try:
        material = await usecase.execute(class_id, material_id)
        if not material:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Material not found"
            )

        return MaterialResponse(
            idMaterial=material.idMaterial,
            idClass=material.idClass,
            title=material.title,
            description=material.description,
            urlFile=material.urlFile,
            urlLink=material.urlLink
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting material: {str(e)}"
        )
