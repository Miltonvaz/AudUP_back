from fastapi import APIRouter, Depends, UploadFile, HTTPException, status
from src.app.transcription.domain.entities.models import CreateTranscriptionModel
from src.app.transcription.infrastructure.dependencies_t.dependencies import init_transcription_dependencies
from src.shared.security.jwt_middleware import validate_jwt
from src.shared.security.auth import Claims

transcription_router = APIRouter()
controllers = init_transcription_dependencies()

def get_current_user(token: str = Depends(validate_jwt)) -> Claims:
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    return token

@transcription_router.post("/transcription", status_code=201, dependencies=[Depends(get_current_user)])
def create_transcription(transcription: CreateTranscriptionModel):
    return controllers["create_transcription_controller"].execute(transcription)

@transcription_router.get("/transcription/{transcription_id}", dependencies=[Depends(get_current_user)])
def get_transcription_by_id(transcription_id: int):
    return controllers["get_transcription_by_id_controller"].execute(transcription_id)

@transcription_router.get("/transcriptions", dependencies=[Depends(get_current_user)])
def get_all_transcriptions():
    return controllers["get_all_transcriptions_controller"].execute()

@transcription_router.put("/transcription/{transcription_id}", dependencies=[Depends(get_current_user)])
def update_transcription(transcription_id: int, transcription_data: CreateTranscriptionModel):
    return controllers["update_transcription_controller"].execute(transcription_id, transcription_data)

@transcription_router.delete("/transcription/{transcription_id}", dependencies=[Depends(get_current_user)])
def delete_transcription(transcription_id: int):
    return controllers["delete_transcription_controller"].execute(transcription_id)

@transcription_router.post("/transcription/upload-pdf", status_code=201, dependencies=[Depends(get_current_user)])
async def upload_transcription_pdf(pdf_file: UploadFile, current_user: Claims = Depends(get_current_user)):
    return await controllers["upload_pdf_controller"].execute(pdf_file, current_user)
