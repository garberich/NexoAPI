from pydantic import BaseModel, EmailStr


class CreateCustomerRequest(BaseModel):
    name: str
    email: EmailStr


class UpdateCustomerRequest(BaseModel):
    name: str
    email: EmailStr


class CustomerResponse(BaseModel):
    id: str
    name: str
    email: str
    is_active: bool
