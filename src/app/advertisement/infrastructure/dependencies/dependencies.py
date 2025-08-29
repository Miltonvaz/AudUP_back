from src.app.advertisement.application.usecase.create_advertisement import CreateAdvertisement
from src.app.advertisement.infrastructure.controllers.create_advertisement import create_advertisement_controller
from src.app.advertisement.infrastructure.db.postgresSQL import PostgreSQLRepository
from src.app.advertisement.application.usecase.get_advertisement import GetAdvertisements
from src.app.advertisement.infrastructure.controllers.get_advertisement import get_advertisements_controller
from src.app.advertisement.application.usecase.get_advertisement_by_id import GetAdvertisementById
from src.app.advertisement.infrastructure.controllers.get_advertisement_by_id import get_advertisement_by_id_controller
from src.app.advertisement.application.usecase.update_advertisement import UpdateAdvertisement
from src.app.advertisement.infrastructure.controllers.update_advertisement import update_advertisement_controller
from src.app.advertisement.application.usecase.delete_advertisement import DeleteAdvertisement
from src.app.advertisement.infrastructure.controllers.delete_advertisement import delete_advertisement_controller


def init_advertisement_dependencies():
    repo = PostgreSQLRepository()
    
    # Use cases
    create_advertisement_usecase = CreateAdvertisement(repo)
    get_advertisements_usecase = GetAdvertisements(repo)
    get_advertisement_by_id_usecase = GetAdvertisementById(repo)
    update_advertisement_usecase = UpdateAdvertisement(repo)
    delete_advertisement_usecase = DeleteAdvertisement(repo)
    
    # Controllers
    def create_advertisement_ctrl(request, claims):
        return create_advertisement_controller(request, create_advertisement_usecase, repo, claims)
    
    def get_advertisements_ctrl(asignature_id, claims):
        return get_advertisements_controller(asignature_id, get_advertisements_usecase, repo)
    
    def get_advertisement_by_id_ctrl(advertisement_id, asignature_id, claims):
        return get_advertisement_by_id_controller(advertisement_id, asignature_id, get_advertisement_by_id_usecase, repo)
    
    def update_advertisement_ctrl(advertisement_id, asignature_id, request, claims):
        return update_advertisement_controller(advertisement_id, asignature_id, request, update_advertisement_usecase, repo, claims)
    
    def delete_advertisement_ctrl(advertisement_id, asignature_id, claims):
        return delete_advertisement_controller(advertisement_id, asignature_id, delete_advertisement_usecase, repo)
    
    return {
        "create_advertisement_controller": create_advertisement_ctrl,
        "get_advertisements_controller": get_advertisements_ctrl,
        "get_advertisement_by_id_controller": get_advertisement_by_id_ctrl,
        "update_advertisement_controller": update_advertisement_ctrl,
        "delete_advertisement_controller": delete_advertisement_ctrl
    }