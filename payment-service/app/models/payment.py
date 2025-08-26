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


class MpesaValidation(BaseModel):
    MerchantRequestID: str | None = None
    CheckoutRequestID: str | None = None
    ResultCode: int | None = None
    ResultDesc: str | None = None


class MpesaConfirmation(BaseModel):
    ResultCode: int | None = None
    ResultDesc: str | None = None
    TransactionType: str | None = None
    TransID: str | None = None
    TransTime: str | None = None
    TransAmount: float | None = None
    BusinessShortCode: str | None = None
    BillRefNumber: str | None = None
    InvoiceNumber: str | None = None
    OrgAccountBalance: str | None = None
    ThirdPartyTransID: str | None = None
    MSISDN: str | None = None
    FirstName: str | None = None
    MiddleName: str | None = None
    LastName: str | None = None
    