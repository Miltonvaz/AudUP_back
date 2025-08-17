from src.app.asignature.application.usecase.create_asignature import CreateAsignature
from src.app.asignature.infrastructure.controllers.create_asignature import CreateAsignatureController
from src.app.asignature.infrastructure.db.postgresSQL import PostgreSQLRepository
from src.app.asignature.application.usecase.update_background import UpdateBackground
from src.app.asignature.infrastructure.controllers.update_background import UpdateBackgroundController

def init_asignature_dependencies():
    repo = PostgreSQLRepository()
    
    #Use cases
    create_asignature_usecase = CreateAsignature(repo)
    update_background_usecase = UpdateBackground(repo)
    
    #Controllers
    create_asignature_controller = CreateAsignatureController(create_asignature_usecase)
    update_background_controller = UpdateBackgroundController(update_background_usecase)
    
    return{
        "create_asignature_controller": create_asignature_controller,
        "update_background_controller": update_background_controller
    }
    
    