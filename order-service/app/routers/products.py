from fastapi import APIRouter
from app.models.product import ProductCreate, Product
from app.db import firestore as repo


router = APIRouter(prefix="/products", tags=["products"])


@router.post("", response_model=Product)
def create_product(payload: ProductCreate):
    doc = repo.create_product(payload.model_dump())
    return Product(**doc)