from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

"""
Choice to use Pydatic so I can achieve data validateion and ORM capabilities,
Also I can use the same schemas for request and response models.
"""

class OrderItem(BaseModel):
    productId: str
    qty: int = Field(gt=0)
    unitPrice: float = Field(ge=0)


class OrderCreate(BaseModel):
    customerId: str
    items: List[OrderItem]
    currency: str = Field(pattern=r"^[A-Z]{3}$")


class Order(BaseModel):
    id: str
    customerId: str
    items: List[OrderItem]
    amount: float
    currency: str
    status: str
    paymentRef: str | None = None
    createdAt: datetime
    updatedAt: datetime
