from datetime import datetime
from pydantic import BaseModel, Field

"""
Choice to use Pydatic so I can achieve data validateion and ORM capabilities,
Also I can use the same schemas for request and response models.
"""

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: float
    currency: str = Field(pattern=r"^[A-Z]{3}$")
    active: bool = True


class Product(ProductCreate):
    id: str
    createdAt: datetime
    updatedAt: datetime

