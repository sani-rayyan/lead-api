from pydantic import BaseModel, Field, EmailStr


class LeadCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    phone: str | None = Field(None, pattern=r"^\d+$")
    service: str | None = None

class LeadUpdate(BaseModel):
    name: str | None = Field(None, min_length=2)
    email: EmailStr | None = None
    phone: str | None = Field(None, pattern=r"^\d+$")
    service: str | None = None
    status: str | None = None

    







