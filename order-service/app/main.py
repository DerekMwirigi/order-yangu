from fastapi import FastAPI
from app.utils import logging
from app.routers import customers, products, orders, internal

app = FastAPI(title="Order-Yangu Services [Orders]", version="1.0.0")
logging.configure_logging()


@app.get("/livez")
def livez():
    return {"status": "ok"}


@app.get("/healthz")
def healthz():
    return {"status": "ok"}

api_version = "v1"

app.include_router(customers.router, prefix=f"/{api_version}")
app.include_router(products.router, prefix=f"/{api_version}")
app.include_router(orders.router, prefix=f"/{api_version}")
app.include_router(internal.router, prefix=f"/{api_version}")
