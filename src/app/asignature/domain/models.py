from pydantic import BaseModel, field_validator, ValidationInfo

# Modelo que llega en el body
class CreateAsignatureRequest(BaseModel):
    name: str
    description: str

    @field_validator('name')
    def name_must_not_be_empty(cls, value, info: ValidationInfo):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value

    @field_validator('description')
    def description_must_not_be_empty(cls, value, info: ValidationInfo):
        if not value.strip():
            raise ValueError("Description cannot be empty")
        return value


# Modelo que ya se usa en la capa de aplicación/repositorio (incluye idUser)
class CreateAsignature(CreateAsignatureRequest):
    idUser: int


# Modelo de respuesta
class CreateAsignatureResponse(BaseModel):
    name: str
    description: str

class UserResponse(BaseModel):
    firstName: str
    secondName: str
    paternalLastName: str
    maternalLastName: str
    email: str