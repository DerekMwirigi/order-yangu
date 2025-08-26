from datetime import datetime
from pydantic import BaseModel, Field

"""
Choice to use Pydatic so I can achieve data validateion and ORM capabilities,
Also I can use the same schemas for request and response models.
"""

class CustomerCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str
    phone: str


class Customer(CustomerCreate):
    id: str
    createdAt: datetime
    updatedAt: datetime

