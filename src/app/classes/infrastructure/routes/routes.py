from fastapi import APIRouter, Depends
from src.shared.security.jwt_middleware import jwt_middleware
from src.shared.security.auth import Claims
from src.app.classes.infrastructure.dependencies.dependencies import init_dependencies_class
from src.app.classes.domain.models import CreateClassRequest

class_router = APIRouter()
controllers = init_dependencies_class()

@class_router.post("/class/{asignature_id}")
def create_class(
    asignature_id : int,
    class_ : CreateClassRequest,
    claims : Claims = Depends(jwt_middleware)
):
    return controllers["create_class_controller"].execute(claims,asignature_id,class_)



