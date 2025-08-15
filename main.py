from fastapi import FastAPI
from src.app.user.infrastructure.routes_u.routes import user_router

app = FastAPI(title="API de Usuarios")


app.include_router(user_router, prefix="/api", tags=["Users"])