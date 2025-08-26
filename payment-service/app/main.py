from fastapi import FastAPI
from app.utils import logging
from app.routers import payments


app = FastAPI(title="Order-Yangu Services [Payments]", version="1.0.0")
logging.configure_logging()


@app.get("/livez")
def livez():
    return {"status": "ok"}


@app.get("/healthz")
def healthz():
# add lightweight checks (e.g., Firestore emulator env var)
    return {"status": "ok"}

api_version = "v1"

app.include_router(payments.router, prefix=f"/{api_version}")
