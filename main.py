from fastapi import FastAPI
from src.app.asignature.infrastructure.routes.routes import asignature_router
from src.app.user.infrastructure.routes_u.routes import user_router
from src.app.transcription.infrastructure.routes_t.routes import transcription_router
from src.app.classes.infrastructure.routes.routes import class_router
from src.app.advertisement.infrastructure.routes.routes import advertisement_router
from src.app.material.infrastructure.routes.routes import material_router

app = FastAPI()

     
app.include_router(asignature_router,prefix="/api/v1", tags=["Asignature"])
app.include_router(user_router, prefix="/api/v1", tags=["Users"])
app.include_router(transcription_router, prefix="/api/v1", tags=["Transcriptions"])
app.include_router(class_router, prefix="/api/v1", tags=["Class"])
app.include_router(advertisement_router, prefix="/api/v1", tags=["Advertisement"])
app.include_router(material_router, prefix="/api/v1", tags=["Material"])