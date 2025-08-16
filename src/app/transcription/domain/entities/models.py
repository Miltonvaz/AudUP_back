from pydantic import BaseModel, field_validator, ValidationInfo
from typing import Optional


class CreateTranscriptionModel(BaseModel):
    idClass: int
    title: str
    content: str

    @field_validator('title')
    def title_must_not_be_empty(cls, value, info: ValidationInfo):
        if not value.strip():
            raise ValueError("Title cannot be empty")
        return value

    @field_validator('content')
    def content_must_not_be_empty(cls, value, info: ValidationInfo):
        if not value.strip():
            raise ValueError("Content cannot be empty")
        return value


class TranscriptionResponse(BaseModel):
    idTranscription: int
    idClass: int
    title: str
    content: str
