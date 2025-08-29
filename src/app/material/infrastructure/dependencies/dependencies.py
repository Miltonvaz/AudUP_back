from src.app.material.application.usecase.create_material import CreateMaterial
from src.app.material.infrastructure.controllers.create_material import create_material_controller
from src.app.material.infrastructure.db.postgresSQL import PostgreSQLRepository
from src.app.material.application.usecase.get_material_by_id import GetMaterialById
from src.app.material.infrastructure.controllers.get_material_by_id import get_material_by_id_controller
from src.app.material.application.usecase.get_materials_by_class import GetMaterialsByClass
from src.app.material.infrastructure.controllers.get_materials_by_class import get_materials_by_class_controller
from src.app.material.application.usecase.update_material import UpdateMaterial
from src.app.material.infrastructure.controllers.update_material import update_material_controller
from src.app.material.application.usecase.delete_material import DeleteMaterial
from src.app.material.infrastructure.controllers.delete_material import delete_material_controller


def init_material_dependencies():
    repo = PostgreSQLRepository()
    
    # Use cases
    create_material_usecase = CreateMaterial(repo)
    get_material_by_id_usecase = GetMaterialById(repo)
    get_materials_by_class_usecase = GetMaterialsByClass(repo)
    update_material_usecase = UpdateMaterial(repo)
    delete_material_usecase = DeleteMaterial(repo)
    
    # Controllers
    def create_material_ctrl(request, claims):
        return create_material_controller(request, create_material_usecase, repo, claims)
    
    def get_material_by_id_ctrl(material_id, class_id, claims):
        return get_material_by_id_controller(material_id, class_id, get_material_by_id_usecase, repo, claims)
    
    def get_materials_by_class_ctrl(class_id, claims):
        return get_materials_by_class_controller(class_id, get_materials_by_class_usecase, repo, claims)
    
    def update_material_ctrl(material_id, class_id, request, claims):
        return update_material_controller(material_id, class_id, request, update_material_usecase, repo, claims)
    
    def delete_material_ctrl(material_id, class_id, claims):
        return delete_material_controller(material_id, class_id, delete_material_usecase, repo, claims)
    
    return {
        "create_material_controller": create_material_ctrl,
        "get_material_by_id_controller": get_material_by_id_ctrl,
        "get_materials_by_class_controller": get_materials_by_class_ctrl,
        "update_material_controller": update_material_ctrl,
        "delete_material_controller": delete_material_ctrl
    }
