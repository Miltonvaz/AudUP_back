from fastapi import FastAPI
from src.app.asignature.infrastructure.routes.routes import asignature_router
from src.app.user.infrastructure.routes_u.routes import user_router

app = FastAPI()

     
app.include_router(asignature_router,prefix="/api/v1", tags=["asignature"])
app.include_router(user_router, prefix="/api/v1", tags=["Users"])