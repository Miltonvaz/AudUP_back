from fastapi import APIRouter, HTTPException, status
from src.app.asignature.infrastructure.db.postgresSQL import PostgreSQLRepository
from src.app.asignature.application.usecase.create_asignature import CreateAsignature
from src.app.asignature.domain.models import CreateAsignatureModel

asignature_router = APIRouter()

@asignature_router.post("/asignature", status_code=status.HTTP_201_CREATED)
def create_asignature(asignature: CreateAsignatureModel):
    repo = PostgreSQLRepository()

    if repo.is_name_taken(asignature.name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There is already a subject with that name"
        )

    try:
        use_case = CreateAsignature(repo)
        return use_case.execute(asignature)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
