from src.app.classes.infrastructure.db.postgreSQL import PosgreSQLRepository
from src.app.classes.application.usecase.create_class import CreateClass
from src.app.classes.infrastructure.controllers.create_class import CreateClassController







def init_dependencies_class():
    repo = PosgreSQLRepository()
    
    #Use cases
    create_class_usecase = CreateClass(repo)
    
    
    #Controllers
    create_class_controller = CreateClassController(create_class_usecase)
    
    
    return {
        "create_class_controller" : create_class_controller
    }
    
    
    
