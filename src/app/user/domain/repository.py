from abc import ABC, abstractmethod
from typing import List, Optional
from src.app.user.domain.entities.models import CreateUserModel


class UserRepository(ABC):

    @abstractmethod
    def create(self, user: CreateUserModel):
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[CreateUserModel]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[CreateUserModel]:
        pass
    @abstractmethod
    def get_all(self) -> List[CreateUserModel]:
        pass

    @abstractmethod
    def update(self, user_id: int, user: CreateUserModel) -> bool:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def is_email_taken(self, email: str) -> bool:
        pass
