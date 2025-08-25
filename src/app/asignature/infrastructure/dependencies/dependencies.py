from src.app.asignature.application.usecase.create_asignature import CreateAsignature
from src.app.asignature.infrastructure.controllers.create_asignature import CreateAsignatureController
from src.app.asignature.infrastructure.db.postgresSQL import PostgreSQLRepository
from src.app.asignature.application.usecase.update_background import UpdateBackground
from src.app.asignature.infrastructure.controllers.update_background import UpdateBackgroundController
from src.app.asignature.application.usecase.update_asignature import UpdateAsignature
from src.app.asignature.infrastructure.controllers.update_asignature import UpdateAsignatureController
from src.app.asignature.application.usecase.delete_asignature import DeleteAsignature
from src.app.asignature.infrastructure.controllers.delete_asignature import DeleteAsignatureController
from src.app.asignature.application.usecase.join_asignature import JoinAsignature
from src.app.asignature.infrastructure.controllers.join_asignature import JoinAsignatureController
from src.app.asignature.application.usecase.get_students import GetStudents
from src.app.asignature.infrastructure.controllers.get_students import GetStudentsController
from src.app.asignature.application.usecase.get_asignatures import GetAsignatures
from src.app.asignature.infrastructure.controllers.get_asignatures import GetAsignaturesController
from src.app.asignature.application.usecase.student_withdraw_from_class import StudentWithdrawFromClass
from src.app.asignature.infrastructure.controllers.student_withdraw_from_class import StudentWithdrawFromClassController
from src.app.asignature.application.usecase.teacher_drops_student_from_class import TeacherDropsStudentFromClass
from src.app.asignature.infrastructure.controllers.teacher_drops_student_from_class import TeacherDropsStudentFromClassController
from src.app.asignature.application.usecase.get_student_asignatures import GetStudentAsignatures
from src.app.asignature.infrastructure.controllers.get_student_asignatures import GetStudentAsignaturesController




def init_asignature_dependencies():
    repo = PostgreSQLRepository()
    
    #Use cases
    create_asignature_usecase = CreateAsignature(repo)
    update_background_usecase = UpdateBackground(repo)
    update_asignature_usecase = UpdateAsignature(repo)
    delete_asignature_usecase = DeleteAsignature(repo)
    join_asignature_usecase   = JoinAsignature(repo)
    get_students_usecase      = GetStudents(repo)
    get_asignatures_usecase   = GetAsignatures(repo)
    student_withdraw_From_class_usecase = StudentWithdrawFromClass(repo)
    teacher_drops_student_from_class_usecase = TeacherDropsStudentFromClass(repo)
    get_student_asignatures_usecase = GetStudentAsignatures(repo)
    
    
    #Controllers
    create_asignature_controller = CreateAsignatureController(create_asignature_usecase)
    update_background_controller = UpdateBackgroundController(update_background_usecase)
    update_asignature_controller = UpdateAsignatureController(update_asignature_usecase)
    delete_asignature_controller = DeleteAsignatureController(delete_asignature_usecase)
    join_asignature_controller   = JoinAsignatureController(join_asignature_usecase)
    get_students_controller      = GetStudentsController(get_students_usecase)
    get_asignatures_controller   = GetAsignaturesController(get_asignatures_usecase)
    student_withdraw_from_class_controller = StudentWithdrawFromClassController(student_withdraw_From_class_usecase)
    teacher_drops_student_from_class_controller = TeacherDropsStudentFromClassController(teacher_drops_student_from_class_usecase)
    get_student_asignatures_controller  = GetStudentAsignaturesController(get_student_asignatures_usecase)
    
    
    return{
        "create_asignature_controller": create_asignature_controller,
        "update_background_controller": update_background_controller,
        "update_asignature_controller":update_asignature_controller,
        "delete_asignature_controller": delete_asignature_controller,
        "join_asignature_controller"  : join_asignature_controller,
        "get_students_controller"     : get_students_controller,
        "get_teacher_asignatures_controller"  : get_asignatures_controller,
        "student_withdraw_from_class_controller" : student_withdraw_from_class_controller,
        "teacher_drops_student_from_class_controller" : teacher_drops_student_from_class_controller,
        "get_student_asignatures_controller" : get_student_asignatures_controller
    }
    
    