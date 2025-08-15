from fastapi import FastAPI
from src.shared.db.database import get_db
from src.app.asignature.infrastructure.routes.routes import asignature_router
app = FastAPI()

@app.get("/")
def func_raiz():
    if get_db():
         return "Jelou"
     
app.include_router(asignature_router,prefix="/api/v1", tags=["asignature"])