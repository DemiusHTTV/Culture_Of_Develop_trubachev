from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Discount Service")

class DiscountRequest(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    promo_code: Optional[str] = None

class DiscountResponse(BaseModel):
    discount_percent: float
    reason: str

@app.post("/discounts/calculate", response_model=DiscountResponse)
def calculate_discount(request: DiscountRequest) -> DiscountResponse:
    if request.promo_code == "STUDENT10":
        return DiscountResponse(discount_percent=10.0, reason="Student promo code applied")
    
    if request.quantity >= 10:
        return DiscountResponse(discount_percent=5.0, reason="Wholesale discount applied (quantity >= 10)")
        
    return DiscountResponse(discount_percent=0.0, reason="No discount applied")
