from pydantic import BaseModel, field_validator, ValidationInfo


class CreateAsignatureModel(BaseModel):
    name: str
    description: str

    @field_validator('name')
    def name_must_not_be_empty(cls, value, info: ValidationInfo):
        if not value:
            raise ValueError("Name cannot be empty")
        return value

    @field_validator('description')
    def description_must_not_be_empty(cls, value, info: ValidationInfo):
        if not value:
            raise ValueError("Description cannot be empty")
        return value


class CreateResponse(BaseModel):
    name: str
    description: str
