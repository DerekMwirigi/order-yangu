from datetime import datetime, timezone
from typing import Any, Dict
from google.cloud import firestore
import os
from app.utils import date_helper, logging

COL_PAYMENTS = "payments"
_client = None

os.environ["FIRESTORE_EMULATOR_HOST"] = os.getenv("PAYMENTS_FIRESTORE_EMULATOR_HOST", "localhost:8085")
project_id = os.getenv("PAYMENTS_FIRESTORE_PROJECT_ID", "order-yangu-payments-dev")

def get_client():
    global _client
    if _client is None:
        _client = firestore.Client(project=project_id)
        logging.logging.debug(f"Firestore client connected to project: {project_id}")
    return _client


def create_payment(doc: Dict[str, Any]) -> Dict[str, Any]:
    db = get_client()
    ref = db.collection(COL_PAYMENTS).document()
    now = date_helper.time_stamp(fmt="utc")
    data = {**doc, "createdAt": now, "updatedAt": now}
    ref.set(data)
    return {"id": ref.id, **data}


def update_payment_status(payment_id: str, status: str, extra: Dict[str, Any] | None = None) -> Dict[str, Any] | None:
    db = get_client()
    ref = db.collection(COL_PAYMENTS).document(payment_id)
    snap = ref.get()
    if not snap.exists:
        return None
    data = snap.to_dict()
    data.update({"status": status, "updatedAt": date_helper.time_stamp(fmt="utc"), **(extra or {})})
    ref.set(data)
    return {"id": payment_id, **data}