from pydantic import BaseModel, field_validator, ValidationInfo, EmailStr
from typing import Optional
from enum import Enum


class UserRole(str, Enum):
    student = "student"
    teacher = "teacher"


class CreateUserModel(BaseModel):
    idRol: UserRole
    firstName: str
    secondName: Optional[str] = None
    paternalLastName: str
    maternalLastName: Optional[str] = None
    email: EmailStr
    passwordHash: str

    @field_validator('firstName')
    def first_name_must_not_be_empty(cls, value, info: ValidationInfo):
        if not value.strip():
            raise ValueError("First name cannot be empty")
        return value

    @field_validator('paternalLastName')
    def paternal_last_name_must_not_be_empty(cls, value, info: ValidationInfo):
        if not value.strip():
            raise ValueError("Paternal last name cannot be empty")
        return value

    @field_validator('passwordHash')
    def password_must_not_be_empty(cls, value, info: ValidationInfo):
        if not value.strip():
            raise ValueError("Password cannot be empty")
        return value


class CreateUserResponse(BaseModel):
    idUser: int
    idRol: UserRole
    firstName: str
    secondName: Optional[str] = None
    paternalLastName: str
    maternalLastName: Optional[str] = None
    email: EmailStr
    createdAt: str
