import os
import httpx


class MpesaClient:
    
    def __init__(self, base_url: str | None = None):
        self.base_url = base_url or os.getenv("MPESA_BASE_URL", "https://sandbox.safaricom.co.ke")
        self.session = httpx.AsyncClient(base_url=self.base_url, timeout=15)


    async def stk_push(self, amount: float, msisdn: str, reference: str) -> dict:
        # TODO: implement Daraja auth + STK push
        return {"MerchantRequestID": "mock-merchant", "CheckoutRequestID": "mock-checkout"}