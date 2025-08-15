from src.app.asignature.application.usecase.create_asignature import CreateAsignature
from src.app.asignature.infrastructure.controllers.create_asignature import CreateAsignatureController
from src.app.asignature.infrastructure.db.postgresSQL import PostgreSQLRepository

def init_asignature_dependencies():
    repo = PostgreSQLRepository()
    
    #Use cases
    create_asignature_usecase = CreateAsignature(repo)
    
    #Controllers
    create_asignature_controller = CreateAsignatureController(create_asignature_usecase)
    
    return{
        "create_asignature_controller":create_asignature_controller
    }
    
    