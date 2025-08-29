from fastapi import HTTPException, status
from src.app.material.application.usecase.update_material import UpdateMaterial
from src.app.material.domain.models import UpdateMaterialRequest, MaterialResponse
from src.app.material.domain.repository import MaterialRepository
from src.shared.security.auth import Claims


async def update_material_controller(
    material_id: int,
    class_id: int,
    request: UpdateMaterialRequest,
    usecase: UpdateMaterial,
    repo: MaterialRepository,
    claims: Claims = None
) -> MaterialResponse:
    """
    Controller para actualizar un material existente en una clase.
    Solo profesores pueden actualizar materiales.
    
    Args:
        material_id (int): ID del material a actualizar
        class_id (int): ID de la clase a la que debe pertenecer el material
        request (UpdateMaterialRequest): Datos de actualización del material
        usecase (UpdateMaterial): Caso de uso para actualizar material
        repo (MaterialRepository): Repositorio de material
        claims (Claims, optional): Claims del JWT con información del usuario
        
    Returns:
        MaterialResponse: Material actualizado
        
    Raises:
        HTTPException: Si el material no existe, no pertenece a la clase,
                       el usuario no es profesor, o hay error de validación
    """
    try:
        if claims and claims.role != "teacher":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only teachers can update materials"
            )

        updated_material = await usecase.execute(material_id, class_id, request)

        if not updated_material:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Material with ID {material_id} not found in class {class_id}"
            )

        return MaterialResponse(
            idMaterial=updated_material.idMaterial,
            idClass=updated_material.idClass,
            title=updated_material.title,
            description=updated_material.description,
            urlFile=updated_material.urlFile,
            urlLink=updated_material.urlLink
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
            detail=f"Error updating material: {str(e)}"
        )
