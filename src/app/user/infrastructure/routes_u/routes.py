from fastapi import APIRouter, Depends, HTTPException, status
from src.app.user.domain.entities.models import CreateUserModel
from src.app.user.infrastructure.dependencies_u.dependencies import init_user_dependencies
from src.shared.security.jwt_middleware import validate_jwt  

user_router = APIRouter()
controllers = init_user_dependencies()

def get_current_user(token: str = Depends(validate_jwt)):
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    return token

@user_router.post("/user", status_code=201)
def create_user(user: CreateUserModel):
    return controllers["create_user_controller"].execute(user)

@user_router.get("/user/{user_id}", dependencies=[Depends(get_current_user)])
def get_user_by_id(user_id: int):
    return controllers["get_user_by_id_controller"].execute(user_id)

@user_router.get("/users", dependencies=[Depends(get_current_user)])
def get_all_users():
    return controllers["get_all_users_controller"].execute()

@user_router.get("/user/email/{email}", dependencies=[Depends(get_current_user)])
def get_user_by_email(email: str):
    return controllers["get_user_by_email_controller"].execute(email)

@user_router.put("/user/{user_id}", dependencies=[Depends(get_current_user)])
def update_user(user_id: int, user_data: CreateUserModel):
    return controllers["update_user_controller"].execute(user_id, user_data)

@user_router.delete("/user/{user_id}", dependencies=[Depends(get_current_user)])
def delete_user(user_id: int):
    return controllers["delete_user_controller"].execute(user_id)

@user_router.post("/login")
def login_user(email: str, password: str):
    return controllers["auth_controller"].execute(email, password)
