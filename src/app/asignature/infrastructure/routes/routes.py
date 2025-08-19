from fastapi import APIRouter, Depends, UploadFile, File
from src.app.asignature.domain.models import CreateAsignatureRequest
from src.app.asignature.infrastructure.dependencies.dependencies import init_asignature_dependencies
from src.shared.security.jwt_middleware import jwt_middleware
from src.shared.security.auth import Claims


asignature_router = APIRouter()
controllers = init_asignature_dependencies()

@asignature_router.post("/asignature", status_code=201)
def create_asignature(
    asignature: CreateAsignatureRequest,
    claims: Claims = Depends(jwt_middleware)  
):
    return controllers["create_asignature_controller"].execute(asignature, claims)

@asignature_router.put("/asignature/{asignature_id}/background", status_code=200)
async def update_background(
    asignature_id : int,
    file : UploadFile = File(...),
    claims : Claims = Depends(jwt_middleware)
):
    return await controllers["update_background_controller"].execute(asignature_id,file,claims)

@asignature_router.put("/asignature/{asignature_id}")
def update_asignature(
    asignature_id : int,
    asignature: CreateAsignatureRequest,
    claims: Claims = Depends(jwt_middleware)
):
    return controllers["update_asignature_controller"].execute(asignature_id,asignature,claims)
@asignature_router.delete("/asignature/{asignature_id}",status_code=200)
def delete_asignature(
    asignature_id : int,
    claims: Claims = Depends(jwt_middleware)
):
    return controllers["delete_asignature_controller"].execute(claims,asignature_id)
