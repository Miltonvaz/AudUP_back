from src.app.user.infrastructure.db.postgresSQL import PostgreSQLRepository
from src.app.user.application.use_case.create_user import CreateUser
from src.app.user.application.use_case.getById_user import GetUserById
from src.app.user.application.use_case.getAll_user import GetAllUser  # <-- Use Case corregido
from src.app.user.application.use_case.getByEmail import GetUserByEmail
from src.app.user.application.use_case.update_user import UpdateUser
from src.app.user.application.use_case.delete_user import DeleteUser
from src.app.user.application.use_case.login import LoginUser

from src.app.user.infrastructure.controllers.create_user import CreateUserController
from src.app.user.infrastructure.controllers.getById import GetUserByIdController
from src.app.user.infrastructure.controllers.getAll import GetAllUsersController
from src.app.user.infrastructure.controllers.getByEmail import GetUserByEmailController
from src.app.user.infrastructure.controllers.update_user import UpdateUserController
from src.app.user.infrastructure.controllers.delete_user import DeleteUserController
from src.app.user.infrastructure.controllers.login import LoginUserController


def init_user_dependencies():
    repo = PostgreSQLRepository()

    create_user_usecase = CreateUser(repo)
    get_user_by_id_usecase = GetUserById(repo)
    get_all_users_usecase = GetAllUser(repo)  
    get_user_by_email_usecase = GetUserByEmail(repo)
    update_user_usecase = UpdateUser(repo)
    delete_user_usecase = DeleteUser(repo)
    login_user_usecase = LoginUser(repo)


    create_user_controller = CreateUserController(create_user_usecase)
    get_user_by_id_controller = GetUserByIdController(get_user_by_id_usecase)
    get_all_users_controller = GetAllUsersController(get_all_users_usecase)
    get_user_by_email_controller = GetUserByEmailController(get_user_by_email_usecase)
    update_user_controller = UpdateUserController(update_user_usecase)
    delete_user_controller = DeleteUserController(delete_user_usecase)
    auth_controller = LoginUserController(login_user_usecase)

    return {
        "create_user_controller": create_user_controller,
        "get_user_by_id_controller": get_user_by_id_controller,
        "get_all_users_controller": get_all_users_controller,
        "get_user_by_email_controller": get_user_by_email_controller,
        "update_user_controller": update_user_controller,
        "delete_user_controller": delete_user_controller,
        "auth_controller": auth_controller
    }
