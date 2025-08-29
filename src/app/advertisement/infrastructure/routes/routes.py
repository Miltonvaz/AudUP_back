from fastapi import APIRouter, Depends
from src.app.advertisement.domain.models import CreateAdvertisementRequest, UpdateAdvertisementRequest
from src.app.advertisement.infrastructure.dependencies.dependencies import init_advertisement_dependencies
from src.shared.security.jwt_middleware import jwt_middleware
from src.shared.security.auth import Claims

advertisement_router = APIRouter()
controllers = init_advertisement_dependencies()

@advertisement_router.post("/asignature/{asignature_id}/advertisement")
async def create_advertisement(
    asignature_id: int,
    advertisement: CreateAdvertisementRequest,
    claims: Claims = Depends(jwt_middleware)
):
    """
    Crea un nuevo advertisement en una asignatura específica
    Solo profesores pueden crear advertisements en sus asignaturas
    """
    # Validar que el idAsignature del request coincida con el path parameter
    if advertisement.idAsignature != asignature_id:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="idAsignature in request body must match asignature_id in URL"
        )
    
    return await controllers["create_advertisement_controller"](advertisement, claims)

@advertisement_router.get("/asignature/{asignature_id}/advertisement")
async def get_advertisements(
    asignature_id: int,
    claims: Claims = Depends(jwt_middleware)
):
    """
    Obtiene todos los advertisements de una asignatura
    Tanto profesores como estudiantes pueden ver los advertisements
    """
    return await controllers["get_advertisements_controller"](asignature_id, claims)

@advertisement_router.get("/asignature/{asignature_id}/advertisement/{advertisement_id}")
async def get_advertisement_by_id(
    asignature_id: int,
    advertisement_id: int,
    claims: Claims = Depends(jwt_middleware)
):
    """
    Obtiene un advertisement específico de una asignatura
    Tanto profesores como estudiantes pueden ver los advertisements
    """
    return await controllers["get_advertisement_by_id_controller"](advertisement_id, asignature_id, claims)

@advertisement_router.put("/asignature/{asignature_id}/advertisement/{advertisement_id}")
async def update_advertisement(
    asignature_id: int,
    advertisement_id: int,
    advertisement: UpdateAdvertisementRequest,
    claims: Claims = Depends(jwt_middleware)
):
    """
    Actualiza un advertisement existente
    Solo profesores pueden actualizar advertisements de sus asignaturas
    """
    return await controllers["update_advertisement_controller"](advertisement_id, asignature_id, advertisement, claims)

@advertisement_router.delete("/asignature/{asignature_id}/advertisement/{advertisement_id}")
async def delete_advertisement(
    asignature_id: int,
    advertisement_id: int,
    claims: Claims = Depends(jwt_middleware)
):
    """
    Elimina un advertisement específico
    Solo profesores pueden eliminar advertisements de sus asignaturas
    """
    return await controllers["delete_advertisement_controller"](advertisement_id, asignature_id, claims)