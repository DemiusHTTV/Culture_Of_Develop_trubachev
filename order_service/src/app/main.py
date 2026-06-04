import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Order Service")

PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://localhost:8001")
DISCOUNT_SERVICE_URL = os.getenv("DISCOUNT_SERVICE_URL", "http://localhost:8000")

class OrderRequest(BaseModel):
    product_id: str
    quantity: int
    promo_code: Optional[str] = None

class OrderResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    amount_before_discount: float
    discount_percent: float
    discount_amount: float
    final_amount: float

@app.post("/orders", response_model=OrderResponse)
async def create_order(request: OrderRequest) -> OrderResponse:
    # 1. Fetch product price
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{PRODUCT_SERVICE_URL}/products/{request.product_id}")
            resp.raise_for_status()
            product_data = resp.json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail="Product not found")
        raise HTTPException(status_code=502, detail="Error communicating with Product Service")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Product Service unavailable: {e}")
        
    unit_price = product_data["price"]
    
    # 2. Get discount
    try:
        async with httpx.AsyncClient() as client:
            discount_payload = {
                "product_id": request.product_id,
                "quantity": request.quantity,
                "unit_price": unit_price,
                "promo_code": request.promo_code
            }
            resp = await client.post(f"{DISCOUNT_SERVICE_URL}/discounts/calculate", json=discount_payload)
            resp.raise_for_status()
            discount_data = resp.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Discount Service unavailable: {e}")
        
    discount_percent = discount_data["discount_percent"]
    
    # 3. Calculations
    amount_before_discount = unit_price * request.quantity
    discount_amount = amount_before_discount * (discount_percent / 100.0)
    final_amount = amount_before_discount - discount_amount
    
    return OrderResponse(
        product_id=request.product_id,
        quantity=request.quantity,
        unit_price=unit_price,
        amount_before_discount=amount_before_discount,
        discount_percent=discount_percent,
        discount_amount=discount_amount,
        final_amount=final_amount
    )
