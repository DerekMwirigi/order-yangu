from fastapi import APIRouter, HTTPException
from app.models.customer import Customer, CustomerCreate
from app.db import firestore as repo

router = APIRouter(prefix="/customers", tags=["customers"])

# post mentod to create a new customer
@router.post("", response_model=Customer)
def create_customer(payload: CustomerCreate):
    doc = repo.create_customer(payload.model_dump())
    if not doc:
        # if customer could not be created, raise an HTTP exception
        raise HTTPException(status_code=400, detail="Customer could not be created")
    # returns object of created customer
    return Customer(**doc)