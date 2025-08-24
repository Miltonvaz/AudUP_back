from src.app.classes.infrastructure.db.postgreSQL import PosgreSQLRepository
from src.app.classes.application.usecase.create_class import CreateClass
from src.app.classes.infrastructure.controllers.create_class import CreateClassController
from src.app.classes.application.usecase.edit_class import EditClass
from src.app.classes.infrastructure.controllers.edit_class import EditClassController








def init_dependencies_class():
    repo = PosgreSQLRepository()
    
    #Use cases
    create_class_usecase = CreateClass(repo)
    edit_class_usecase   = EditClass(repo)
    
    
    #Controllers
    create_class_controller = CreateClassController(create_class_usecase)
    edit_class_controller   = EditClassController(edit_class_usecase)
    
    
    return {
        "create_class_controller" : create_class_controller,
        "edit_class_controller"   : edit_class_controller
    }
    
    
    
