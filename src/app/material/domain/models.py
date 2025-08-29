from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class MaterialBase(BaseModel):
    """Modelo base para Material"""
    title: str = Field(..., max_length=255, description="Título del material")
    description: Optional[str] = Field(None, max_length=500, description="Descripción del material")
    urlFile: str = Field(..., description="URL del archivo")
    urlLink: Optional[str] = Field(None, description="URL de enlace adicional")

class CreateMaterialRequest(MaterialBase):
    """Modelo para crear un material"""
    idClass: int = Field(..., description="ID de la clase a la que pertenece el material")

class UpdateMaterialRequest(BaseModel):
    """Modelo para actualizar un material"""
    title: Optional[str] = Field(None, max_length=255, description="Título del material")
    description: Optional[str] = Field(None, max_length=500, description="Descripción del material")
    urlFile: Optional[str] = Field(None, description="URL del archivo")
    urlLink: Optional[str] = Field(None, description="URL de enlace adicional")

class MaterialResponse(MaterialBase):
    """Modelo de respuesta para Material"""
    idMaterial: int
    idClass: int
    
    class Config:
        from_attributes = True

class Material(MaterialBase):
    """Entidad Material del dominio"""
    idMaterial: int
    idClass: int