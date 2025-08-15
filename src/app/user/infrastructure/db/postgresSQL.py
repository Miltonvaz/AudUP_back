from typing import List, Optional
from src.shared.db.database import get_db
from src.app.user.domain.repository import UserRepository
from src.app.user.domain.entities.models import CreateUserModel
from src.shared.db.orm_models import User 


class PostgreSQLRepository(UserRepository):
    def __init__(self):
        self.connection = next(get_db())
        if not self.connection:
            print("Error al obtener la conexión")
            return None

    def create(self, user: CreateUserModel) -> User:
        new_user = User(**user.dict())
        self.connection.add(new_user)
        self.connection.commit()
        self.connection.refresh(new_user)
        return new_user

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.connection.query(User).filter(User.idUser == user_id).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.connection.query(User).filter(User.email == email).first()

    def get_all(self) -> List[User]:
        return self.connection.query(User).all()


    def update(self, user_id: int, user: CreateUserModel) -> Optional[User]:
        existing_user = self.connection.query(User).filter(User.idUser == user_id).first()
        if not existing_user:
            return None
        for key, value in user.dict(exclude_unset=True).items():
            setattr(existing_user, key, value)
        self.connection.commit()
        self.connection.refresh(existing_user)
        return existing_user

    def delete(self, user_id: int) -> bool:
        user = self.connection.query(User).filter(User.idUser == user_id).first()
        if not user:
            return False
        self.connection.delete(user)
        self.connection.commit()
        return True

    def is_email_taken(self, email: str) -> bool:
        return self.connection.query(User).filter(User.email == email).first() is not None
