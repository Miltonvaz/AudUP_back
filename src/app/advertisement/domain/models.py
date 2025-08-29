from pydantic import BaseModel, field_validator, ValidationInfo
from typing import Optional
from datetime import date


# Modelo que llega en el body
class CreateAdvertisementRequest(BaseModel):
    idAsignature: int
    name: str
    description: Optional[str] = None

    @field_validator('name')
    def name_must_not_be_empty(cls, value, info: ValidationInfo):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value


# Modelo usado en capa aplicación/repositorio
class CreateAdvertisement(CreateAdvertisementRequest):
    pass


# Modelo para actualización
class UpdateAdvertisementRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    @field_validator('name')
    def name_must_not_be_empty(cls, value, info: ValidationInfo):
        if value is not None and not value.strip():
            raise ValueError("Name cannot be empty")
        return value


# Modelo de dominio principal
class Advertisement(BaseModel):
    idAdvertisement: Optional[int] = None  # None para creación, int después de guardar
    idAsignature: int
    name: str
    description: Optional[str] = None
    date: Optional[date] = None  # Se asigna al crear en BD


# Modelo de respuesta
class AdvertisementResponse(BaseModel):
    idAdvertisement: int
    idAsignature: int
    name: str
    description: Optional[str] = None
    date: date