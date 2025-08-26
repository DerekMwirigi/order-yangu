from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal


class PaymentCreate(BaseModel):
    orderId: str
    msisdn: str = Field(min_length=10, max_length=15)
    amount: float
    idempotencyKey: str | None = None


class Payment(BaseModel):
    id: str
    orderId: str
    amount: float
    currency: str
    status: str
    createdAt: datetime
    updatedAt: datetime


class MpesaCallback(BaseModel):
    MerchantRequestID: str | None = None
    CheckoutRequestID: str | None = None
    ResultCode: int | None = None
    ResultDesc: str | None = None