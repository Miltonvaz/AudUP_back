from fastapi import FastAPI
from src.app.asignature.infrastructure.routes.routes import asignature_router
from src.app.user.infrastructure.routes_u.routes import user_router
from src.app.classes.infrastructure.routes.routes import class_router



app = FastAPI()

     
app.include_router(asignature_router,prefix="/api/v1", tags=["Asignature"])
app.include_router(user_router, prefix="/api/v1", tags=["Users"])
app.include_router(class_router, prefix="/api/v1", tags=["Class"])