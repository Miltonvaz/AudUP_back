from fastapi import HTTPException, status
from src.app.material.application.usecase.create_material import CreateMaterial
from src.app.material.domain.models import CreateMaterialRequest, MaterialResponse
from src.app.material.domain.repository import MaterialRepository
from src.shared.security.auth import Claims


async def create_material_controller(
    request: CreateMaterialRequest,
    usecase: CreateMaterial,
    repo: MaterialRepository,
    claims: Claims = None
) -> MaterialResponse:
    """
    Controller para crear un nuevo material dentro de una clase.
    Solo profesores pueden crear materiales.
    
    Args:
        request: Datos del material a crear
        usecase: Caso de uso para crear material
        repo: Repositorio de material
        claims: Claims del JWT con información del usuario
        
    Returns:
        MaterialResponse: Material creado
        
    Raises:
        HTTPException: Si ocurre un error durante la creación
    """
    try:
        # Validar que el usuario es profesor
        if claims and claims.role != "teacher":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only teachers can create materials"
            )
        
        # Ejecutar caso de uso
        created_material = await usecase.execute(request)
        
        # Mapear a response
        return MaterialResponse(
            idMaterial=created_material.idMaterial,
            idClass=created_material.idClass,
            title=created_material.title,
            description=created_material.description,
            urlFile=created_material.urlFile,
            urlLink=created_material.urlLink
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
            detail=f"Error creating material: {str(e)}"
        )
