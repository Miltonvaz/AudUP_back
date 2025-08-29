from fastapi import HTTPException, status
from src.app.material.application.usecase.delete_material import DeleteMaterial
from src.app.material.domain.repository import MaterialRepository
from src.shared.security.auth import Claims


async def delete_material_controller(
    material_id: int,
    class_id: int,
    usecase: DeleteMaterial,
    repo: MaterialRepository,
    claims: Claims = None
) -> dict:
    """
    Controller para eliminar un material existente en una clase.
    Solo profesores pueden eliminar materiales.
    
    Args:
        material_id (int): ID del material a eliminar
        class_id (int): ID de la clase a la que debe pertenecer el material
        usecase (DeleteMaterial): Caso de uso para eliminar material
        repo (MaterialRepository): Repositorio de material
        claims (Claims, optional): Claims del JWT con información del usuario
        
    Returns:
        dict: Mensaje de confirmación de eliminación con IDs
        
    Raises:
        HTTPException: Si el material no existe, no pertenece a la clase
                       o el usuario no tiene permisos
    """
    try:
        if claims and claims.role != "teacher":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only teachers can delete materials"
            )

        deleted = await usecase.execute(material_id, class_id)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Material with ID {material_id} not found in class {class_id}"
            )

        return {
            "message": f"Material {material_id} deleted successfully",
            "idMaterial": material_id,
            "idClass": class_id
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting material: {str(e)}"
        )
