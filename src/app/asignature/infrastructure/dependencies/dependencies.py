from src.app.asignature.application.usecase.create_asignature import CreateAsignature
from src.app.asignature.infrastructure.controllers.create_asignature import CreateAsignatureController
from src.app.asignature.infrastructure.db.postgresSQL import PostgreSQLRepository
from src.app.asignature.application.usecase.update_background import UpdateBackground
from src.app.asignature.infrastructure.controllers.update_background import UpdateBackgroundController
from src.app.asignature.application.usecase.update_asignature import UpdateAsignature
from src.app.asignature.infrastructure.controllers.update_asignature import UpdateAsignatureController
from src.app.asignature.application.usecase.delete_asignature import DeleteAsignature
from src.app.asignature.infrastructure.controllers.delete_asignature import DeleteAsignatureController

def init_asignature_dependencies():
    repo = PostgreSQLRepository()
    
    #Use cases
    create_asignature_usecase = CreateAsignature(repo)
    update_background_usecase = UpdateBackground(repo)
    update_asignature_usecase = UpdateAsignature(repo)
    delete_asignature_usecase = DeleteAsignature(repo)
    
    #Controllers
    create_asignature_controller = CreateAsignatureController(create_asignature_usecase)
    update_background_controller = UpdateBackgroundController(update_background_usecase)
    update_asignature_controller = UpdateAsignatureController(update_asignature_usecase)
    delete_asignature_controller = DeleteAsignatureController(delete_asignature_usecase)
    
    return{
        "create_asignature_controller": create_asignature_controller,
        "update_background_controller": update_background_controller,
        "update_asignature_controller":update_asignature_controller,
        "delete_asignature_controller": delete_asignature_controller
    }
    
    