from src.app.transcription.infrastructure.db.postgresSQL import PostgreSQLTranscriptionRepository
from src.app.transcription.application.use_case.create_transcription import CreateTranscription
from src.app.transcription.application.use_case.getById_transcription import GetTranscriptionById
from src.app.transcription.application.use_case.getAll_transcription import GetAllTranscription  
from src.app.transcription.application.use_case.update_transcription import UpdateTranscription
from src.app.transcription.application.use_case.delete_transcription import DeleteTranscription

from src.app.transcription.infrastructure.controllers.create_transcription import CreateTranscriptionController
from src.app.transcription.infrastructure.controllers.getById_transcription import GetTranscriptionByIdController
from src.app.transcription.infrastructure.controllers.getAll_transcription import GetAllTranscriptionController
from src.app.transcription.infrastructure.controllers.update_transcription import UpdateTranscriptionController
from src.app.transcription.infrastructure.controllers.delete_transcription import DeleteTranscriptionController


def init_transcription_dependencies():
    repo = PostgreSQLTranscriptionRepository()

    create_transcription_usecase = CreateTranscription(repo)
    get_transcription_by_id_usecase = GetTranscriptionById(repo)
    get_all_transcriptions_usecase = GetAllTranscription(repo)  
    update_transcription_usecase = UpdateTranscription(repo)
    delete_transcription_usecase = DeleteTranscription(repo)

    create_transcription_controller = CreateTranscriptionController(create_transcription_usecase)
    get_transcription_by_id_controller = GetTranscriptionByIdController(get_transcription_by_id_usecase)
    get_all_transcriptions_controller = GetAllTranscriptionController(get_all_transcriptions_usecase)
    update_transcription_controller = UpdateTranscriptionController(update_transcription_usecase)
    delete_transcription_controller = DeleteTranscriptionController(delete_transcription_usecase)
  
    return {
        "create_transcription_controller": create_transcription_controller,
        "get_transcription_by_id_controller": get_transcription_by_id_controller,
        "get_all_transcriptions_controller": get_all_transcriptions_controller,
        "update_transcription_controller": update_transcription_controller,
        "delete_transcription_controller": delete_transcription_controller
    }
