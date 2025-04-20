from fastapi import APIRouter
from datetime import datetime
from backend.models.purchase import Purchase


router = APIRouter()

@router.get("/customer-report")
async def customer_report():
    today = datetime.now()

    pipeline = [
        {
            "$group": {
                "_id": "$customer_id",
                "total_spend": {"$sum": "$amount"},
                "number_of_orders": {"$sum": 1},
                "last_purchase": {"$max": "$order_date"}
            }
        },
        {
            "$addFields": {
                "average_order_value": {
                    "$divide": ["$total_spend", "$number_of_orders"]
                },
                "recency_days": {
                    "$dateDiff": {
                        "startDate": "$last_purchase",
                        "endDate": today,
                        "unit": "day"
                    }
                },
                "high_value_customer": {
                    "$and": [
                        {"$gt": ["$total_spend", 500]},
                        {"$lt": [
                            {
                                "$dateDiff": {
                                    "startDate": "$last_purchase",
                                    "endDate": today,
                                    "unit": "day"
                                }
                            },
                            30
                        ]}
                    ]
                }
            }
        }
    ]

    result = await Purchase.aggregate(pipeline).to_list()
    return result
