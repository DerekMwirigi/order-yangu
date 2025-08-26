from fastapi import APIRouter, HTTPException
from app.models.payment import PaymentCreate, Payment, MpesaCallback
from app.db import firestore as repo
from app.mpesa.client import MpesaClient
import os
import httpx


router = APIRouter(prefix="/payments", tags=["payments"])


ORDERS_INTERNAL_URL = os.getenv("ORDERS_INTERNAL_URL", "http://orders:8080/v1")


@router.post("", response_model=Payment)
async def create_payment(payload: PaymentCreate):
    """
    TODO: Check if order exists, make call to order's service
    """

    payment = repo.create_payment({
        "orderId": payload.orderId,
        "amount": payload.amount,
        "currency": "KES",
        "status": "INITIATED",
        "idempotencyKey": payload.idempotencyKey,
    })
    client = MpesaClient()
    # mock daraja api skt push
    _resp = await client.stk_push(amount=payload.amount, msisdn=payload.msisdn, reference=payment["id"])
    return Payment(**payment)


@router.post("/mpesa")
async def mpesa_callback(cb: MpesaCallback):
    # TODO: verify signature
    # Map result to payment status
    status = "SUCCESS" if (cb.ResultCode == 0) else "FAILED"
    # Suppose reference is embedded in CheckoutRequestID mapping (mock). In real, you would persist mapping.
    payment_id = cb.CheckoutRequestID or "unknown"
    updated = repo.update_payment_status(payment_id, status, extra={"rawWebhook": cb.model_dump()})
    
    # call Orders service to mark paid on success
    if status == "SUCCESS":
        try:
            # use async
            async with httpx.AsyncClient(timeout=10) as client:
                await client.post(f"{ORDERS_INTERNAL_URL}/orders/{updated['orderId']}:mark-paid")
        except Exception:
            pass
            """TODO: Adding error logging rollbar"""

    return {"status": status}