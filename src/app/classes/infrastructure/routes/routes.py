from fastapi import APIRouter, Depends
from src.shared.security.jwt_middleware import jwt_middleware
from src.shared.security.auth import Claims
from src.app.classes.infrastructure.dependencies.dependencies import init_dependencies_class
from src.app.classes.domain.models import CreateClassRequest

class_router = APIRouter()
controllers = init_dependencies_class()

@class_router.post("/asignature/{asignature_id}/class")
def create_class(
    asignature_id : int,
    class_ : CreateClassRequest,
    claims : Claims = Depends(jwt_middleware)
):
    return controllers["create_class_controller"].execute(claims,asignature_id,class_)

@class_router.put("/asignature/{asignature_id}/class/{class_id}")
def edit_class(
    asignature_id : int,
    class_ : CreateClassRequest,
    class_id :int,
    claims : Claims = Depends(jwt_middleware)
):
    return controllers["edit_class_controller"].execute(claims,asignature_id,class_id,class_)



