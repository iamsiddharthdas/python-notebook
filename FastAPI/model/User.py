from pydantic import BaseModel, Field,EmailStr

from datetime import datetime
class User(BaseModel):
    username: str = Field(..., example="JohnDoe", min_length=3, max_length=20)
    password: str = Field(..., example="securePass123", min_length=6, max_length=20)
    cpassword: str = Field(..., example="securePass123", min_length=6, max_length=20)
    email: EmailStr = Field(..., example="john@example.com", min_length=6, max_length=50)
    pno: str = Field(..., example="1234567890", min_length=10, max_length=15)
    dateofadd: datetime = Field(default_factory=datetime.now, example="2024-12-31T12:34:56")