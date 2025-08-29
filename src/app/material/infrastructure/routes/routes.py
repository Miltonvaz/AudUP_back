from fastapi import APIRouter, Depends, HTTPException, status
from src.app.material.domain.models import CreateMaterialRequest, UpdateMaterialRequest
from src.app.material.infrastructure.dependencies.dependencies import init_material_dependencies
from src.shared.security.jwt_middleware import jwt_middleware
from src.shared.security.auth import Claims

material_router = APIRouter()
controllers = init_material_dependencies()

@material_router.post("/class/{class_id}/material")
async def create_material(
    class_id: int,
    material: CreateMaterialRequest,
    claims: Claims = Depends(jwt_middleware)
):
    """
    Crea un nuevo material en una clase específica
    Solo profesores pueden crear materiales en sus clases
    """
    # Validar que el idClass del request coincida con el path parameter
    if material.idClass != class_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="idClass in request body must match class_id in URL"
        )
    return await controllers["create_material_controller"](material, claims)

@material_router.get("/class/{class_id}/material")
async def get_materials_by_class(
    class_id: int,
    claims: Claims = Depends(jwt_middleware)
):
    """
    Obtiene todos los materiales de una clase
    Tanto profesores como estudiantes pueden ver los materiales
    """
    return await controllers["get_materials_by_class_controller"](class_id, claims)

@material_router.get("/class/{class_id}/material/{material_id}")
async def get_material_by_id(
    class_id: int,
    material_id: int,
    claims: Claims = Depends(jwt_middleware)
):
    """
    Obtiene un material específico de una clase
    Tanto profesores como estudiantes pueden ver los materiales
    """
    return await controllers["get_material_by_id_controller"](material_id, class_id, claims)

@material_router.put("/class/{class_id}/material/{material_id}")
async def update_material(
    class_id: int,
    material_id: int,
    material: UpdateMaterialRequest,
    claims: Claims = Depends(jwt_middleware)
):
    """
    Actualiza un material existente
    Solo profesores pueden actualizar materiales de sus clases
    """
    return await controllers["update_material_controller"](material_id, class_id, material, claims)

@material_router.delete("/class/{class_id}/material/{material_id}")
async def delete_material(
    class_id: int,
    material_id: int,
    claims: Claims = Depends(jwt_middleware)
):
    """
    Elimina un material específico
    Solo profesores pueden eliminar materiales de sus clases
    """
    return await controllers["delete_material_controller"](material_id, class_id, claims)
