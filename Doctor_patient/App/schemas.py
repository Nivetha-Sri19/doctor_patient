from pydantic import BaseModel, EmailStr
from typing import Optional

# Doctor Schema
class DoctorBase(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: Optional[bool] = True


class DoctorCreate(DoctorBase):
    pass


class Doctor(DoctorBase):
    id: int


# Patient Schema
class PatientBase(BaseModel):
    name: str
    age: int
    phone: str

    # validation
    @classmethod
    def validate_age(cls, value):
        if value <= 0:
            raise ValueError("Age must be greater than 0")
        return value


class PatientCreate(PatientBase):
    pass


class Patient(PatientBase):
    id: int