from beanie import Document
from pydantic import BaseModel
from datetime import datetime

class Purchase(Document):
    customer_id: str
    order_id: str
    order_date: datetime
    amount: float

    class Settings:
        name = "purchases"
