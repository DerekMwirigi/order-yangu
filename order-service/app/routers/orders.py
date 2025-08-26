from fastapi import APIRouter, HTTPException
from app.models.order import OrderCreate, Order, OrderItem
from app.db import firestore as repo


router = APIRouter(prefix="/orders", tags=["orders"])

# post methode to create a new order
@router.post("", response_model=Order)
def create_order(payload: OrderCreate):
    # calculate total amount
    amount = sum(i.qty * i.unitPrice for i in payload.items if i.qty > 0 and i.unitPrice >= 0) if len(payload.items) > 0 else 0.0
    # default status is PENDING
    doc = repo.create_order({
        "customerId": payload.customerId,
        "items": [i.model_dump() for i in payload.items],
        "amount": round(amount, 2),
        "currency": payload.currency,
        "status": "PENDING",
    })
    return Order(**doc)

# get method to fetch an order by ID
@router.get("/{order_id}", response_model=Order)
def get_order(order_id: str):
    doc = repo.get_order(order_id)
    if not doc:
        raise HTTPException(404, "Order not found")
    return Order(**doc)

# get method to fetch all orders with optional filters and pagination
@router.get("", response_model=list[Order])
def list_orders(filter_status: str | None = None, skip: int = 0, limit: int = 10):
    docs = repo.list_orders(
        filters=filter_status if filter_status else None,
        order_by=("createdAt", "desc"),
        limit=limit,
        start_after=skip if skip > 0 else None,
    )
    return [Order(**doc) for doc in docs]

