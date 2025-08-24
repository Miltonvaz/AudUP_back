from pydantic import BaseModel, field_validator, ValidationInfo
from datetime import date



class CreateClassRequest(BaseModel):
    name: str
    
    @field_validator('name')
    def name_must_not_be_empty(cls, value, info: ValidationInfo):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value
    
    
class CreateClassResponse(BaseModel):
    class_id : int
    name : str
    date : date

    
    

    
    
    
    