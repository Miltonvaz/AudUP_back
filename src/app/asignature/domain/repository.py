from abc import ABC, abstractmethod
from src.app.asignature.domain.models import CreateAsignatureRequest, CreateAsignatureResponse, UserResponse, TeacherAsignatureResponse
from typing import List


class AsignatureRepository(ABC):
    @abstractmethod
    def create(self, asignature: CreateAsignatureRequest, user_id: int) -> CreateAsignatureResponse:
        pass

    @abstractmethod
    def is_name_taken(self, name: str) -> bool:
        pass

    @abstractmethod
    def update_background(self, asignature_id: int, background_url: str, user_id: int):
        pass

    @abstractmethod
    def update(self, asignature: CreateAsignatureRequest, user_id: int, asignature_id: int) -> CreateAsignatureResponse:
        pass

    @abstractmethod
    def exists_asignature(self, user_id: int, asignature_id: int) -> bool:
        pass

    @abstractmethod
    def delete(self, user_id: int, asignature_id: int)->bool:
        pass
    @abstractmethod
    def join_asignature(self,user_id, asignature_id)->str:
        pass
    @abstractmethod
    def get_students(self,user_id: int, asignature_id: int)->List[UserResponse]:
        pass
    @abstractmethod
    def get_asignatures(self, user_id: int)->List[TeacherAsignatureResponse]:
        pass
    @abstractmethod
    def student_withdraw_from_class(self,user_id: int, asignature :int)->str:
        pass
    @abstractmethod
    def teacher_drops_student_from_class(self, asignature_id: int, student_id : int)->str:
        pass
    @abstractmethod
    def get_student_asignatures(self, user_id : int)->List[TeacherAsignatureResponse]:
        pass