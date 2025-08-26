import os
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple
from google.cloud import firestore
from app.utils import date_helper

COL_CUSTOMERS = "customers"
COL_PRODUCTS = "products"
COL_ORDERS = "orders"


_client = None

os.environ["FIRESTORE_EMULATOR_HOST"] = os.getenv("ORDERS_FIRESTORE_EMULATOR_HOST", "localhost:8085")
project_id = os.getenv("ORDERS_FIRESTORE_PROJECT_ID", "order-yangu-orders-dev")

def get_client(): 
    global _client
    if _client is None:
        _client = firestore.Client( project=project_id)
        print(f"Firestore client connected to project: {project_id}")
        
    return _client


# Customer repo
def create_customer(data: Dict[str, Any]) -> Dict[str, Any]:
    db = get_client()
    ref = db.collection(COL_CUSTOMERS).document()
    now = date_helper.time_stamp()
    doc = {**data, "createdAt": now, "updatedAt": now}
    ref.set(doc)
    return {"id": ref.id, **doc}


# Product repo
def create_product(data: Dict[str, Any]) -> Dict[str, Any]:
    db = get_client()
    ref = db.collection(COL_PRODUCTS).document()
    now = date_helper.time_stamp()
    doc = {**data, "createdAt": now, "updatedAt": now}
    ref.set(doc)
    return {"id": ref.id, **doc}


# Order repo
def create_order(data: Dict[str, Any]) -> Dict[str, Any]:
    db = get_client()
    ref = db.collection(COL_ORDERS).document()
    now = date_helper.time_stamp()
    doc = {**data, "createdAt": now, "updatedAt": now}
    ref.set(doc)
    return {"id": ref.id, **doc}

def get_order(order_id: str) -> Dict[str, Any] | None:
    db = get_client()
    snap = db.collection(COL_ORDERS).document(order_id).get()
    return {"id": snap.id, **snap.to_dict()} if snap.exists else None

# List orders with optional filtering by status and pagination
def list_orders(filters: Optional[Dict[str, Any]] = None,
    order_by: Optional[Tuple[str, str]] = None,  # e.g. ("createdAt", "desc")
    limit: int = 20,
    start_after: Optional[Any] = None,  # pass last seen value for pagination
) -> List[Dict[str, Any]]:
    
    db = get_client()
    query = db.collection(COL_ORDERS)

    # Apply filters (AND conditions)
    if filters:
        for field, value in filters.items():
            if isinstance(value, tuple) and len(value) == 2:
                # example: filters={"createdAt": (">=", some_date)}
                op, val = value
                query = query.where(field, op, val)
            else:
                query = query.where(field, "==", value)

    # Sorting
    if order_by:
        # order_by is a tuple (field, direction)
        field, direction = order_by
        query = query.order_by(
            field,
            direction=firestore.Query.DESCENDING
            if direction.lower() == "desc"
            else firestore.Query.ASCENDING,
        )

    # Pagination
    if start_after:
        query = query.start_after({order_by[0]: start_after}) if order_by else query.start_after(start_after)

    # Limit
    query = query.limit(limit)

    # Execute
    orders = query.stream()

    return [{"id": order.id, **order.to_dict()} for order in orders]



def mark_order_paid(order_id: str) -> Dict[str, Any] | None:
    db = get_client()
    doc_ref = db.collection(COL_ORDERS).document(order_id)
    
    # function to perform order update in a transaction
    def txn(tx):
        snap = doc_ref.get(transaction=tx)
        if not snap.exists:
            return None
        doc = snap.to_dict()
        if doc.get("status") != "PAID":
            doc["status"] = "PAID"
            doc["updatedAt"] = date_helper.time_stamp()
            tx.set(doc_ref, doc)
            return {"id": snap.id, **doc}
        
    return db.transaction()(txn)