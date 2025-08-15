from typing import List, Optional
from fastapi import HTTPException, status
from src.shared.db.database import get_db
from src.app.user.domain.repository import UserRepository
from src.app.user.domain.entities.models import CreateUserModel
from src.shared.db.orm_models import User
from sqlalchemy.exc import IntegrityError

class PostgreSQLRepository(UserRepository):
    def __init__(self):
        self.connection = next(get_db())
        if not self.connection:
            print("Error al obtener la conexión")
            return None

    def create(self, user: CreateUserModel) -> User:
        new_user = User(**user.dict())
        try:
            self.connection.add(new_user)
            self.connection.commit()
            self.connection.refresh(new_user)
            return new_user
        except IntegrityError as e:
            # Si falla por UNIQUE u otra violación de integridad
            self.connection.rollback()
            if 'User_email_key' in str(e.orig):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists"
                )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error"
            )
        except Exception:
            self.connection.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error"
            )

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
        try:
            for key, value in user.dict(exclude_unset=True).items():
                setattr(existing_user, key, value)
            self.connection.commit()
            self.connection.refresh(existing_user)
            return existing_user
        except IntegrityError as e:
            self.connection.rollback()
            if 'User_email_key' in str(e.orig):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists"
                )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error"
            )
        except Exception:
            self.connection.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error"
            )

    def delete(self, user_id: int) -> bool:
        user = self.connection.query(User).filter(User.idUser == user_id).first()
        if not user:
            return False
        try:
            self.connection.delete(user)
            self.connection.commit()
            return True
        except Exception:
            self.connection.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error"
            )

    def is_email_taken(self, email: str) -> bool:
        return self.connection.query(User).filter(User.email == email).first() is not None
