
from pydantic import BaseModel, EmailStr, Field
from datetime import date


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    dob: date
    email: EmailStr
    phone: str | None = None
    course: str | None = None
    address: str | None = None


class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    dob: date | None = None
    email: EmailStr | None = None
    phone: str | None = None
    course: str | None = None
    address: str | None = None
