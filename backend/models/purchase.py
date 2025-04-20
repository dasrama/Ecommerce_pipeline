from beanie import Document
from pydantic import BaseModel
from datetime import datetime

class Purchase(Document, BaseModel):
    customer_id: str
    order_id: str
    order_date: datetime
    amount: float
    category: str
     
    class Settings:
        name = "purchases"
