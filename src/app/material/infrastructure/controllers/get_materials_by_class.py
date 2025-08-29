from fastapi import HTTPException, status
from src.app.material.application.usecase.get_materials_by_class import GetMaterialsByClass
from src.app.material.domain.models import MaterialResponse
from src.app.material.domain.repository import MaterialRepository
from typing import List
from src.shared.security.auth import Claims


async def get_materials_by_class_controller(
    class_id: int,
    usecase: GetMaterialsByClass,
    repo: MaterialRepository,
    claims: Claims = None
) -> List[MaterialResponse]:
    """
    Controller para obtener todos los materiales de una clase.
    
    Args:
        class_id: ID de la clase
        usecase: Caso de uso para obtener materiales
        repo: Repositorio de material
        claims: Claims del JWT con información del usuario
        
    Returns:
        List[MaterialResponse]: Lista de materiales de la clase
    """
    try:
        materials = await usecase.execute(class_id)

        return [
            MaterialResponse(
                idMaterial=m.idMaterial,
                idClass=m.idClass,
                title=m.title,
                description=m.description,
                urlFile=m.urlFile,
                urlLink=m.urlLink
            ) for m in materials
        ]

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting materials: {str(e)}"
        )
