from fastapi import APIRouter, Header, HTTPException
from app.db import firestore as repo
# TODO: verify Google OIDC token from Payments service via Authorization header


router = APIRouter(prefix="/orders", tags=["internal"]) # share tag


@router.post("/{order_id}:mark-paid")
def mark_paid(order_id: str, authorization: str | None = Header(default=None)):
    # TODO: verify JWT aud/iss (Cloud Run)
    doc = repo.mark_order_paid(order_id)
    if not doc:
        raise HTTPException(404, "Order not found")
    return {"status": "ok", "order": doc}