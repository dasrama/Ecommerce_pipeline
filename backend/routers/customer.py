from fastapi import APIRouter, Query
from datetime import datetime, timedelta
from backend.models.purchase import Purchase
import io
import openpyxl
from fastapi.responses import StreamingResponse


router = APIRouter()

def generate_excel(data):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Customer Report"
    
    headers = ["customerId", "totalSpent", "averageOrderValue", "orderCount", "loyaltyTier", "lastPurchaseDate", "isActive"]
    sheet.append(headers)

    for row in data:
        sheet.append([row["customerId"], row["totalSpent"], row["averageOrderValue"], row["orderCount"], row["loyaltyTier"], row["lastPurchaseDate"], row["isActive"]])

    excel_file = io.BytesIO()
    workbook.save(excel_file)
    excel_file.seek(0)

    return excel_file


@router.get("/report")
async def customer_report(min_total_spent: float = Query(0.0, ge=0)):
    six_months_ago = datetime.now() - timedelta(days=180)

    pipeline = [
        {
            "$group": {
                "_id": "$customer_id",
                "totalSpent": {"$sum": "$amount"},
                "averageOrderValue": {"$avg": "$amount"}, 
                "orderCount": {"$sum": 1},
                "lastPurchaseDate": {"$max": "$order_date"}
            }
        },
        {
            "$addFields": {
                "lastPurchaseDate": { "$toDate": "$lastPurchaseDate" },  
                "isActive": {
                    "$gte": [
                        {"$toDate": "$lastPurchaseDate"},  
                        six_months_ago  
                    ]
                },
                "loyaltyTier": {
                    "$switch": {
                        "branches": [
                            {
                                "case": {"$lt": ["$totalSpent", 1000]}, 
                                "then": "Bronze"
                            },
                            {
                                "case": {"$and": [{"$gte": ["$totalSpent", 1000]}, {"$lte": ["$totalSpent", 3000]}]},
                                "then": "Silver"
                            },
                            {
                                "case": {"$gt": ["$totalSpent", 3000]}, 
                                "then": "Gold"
                            }
                        ],
                        "default": "Bronze"  
                    }
                }
            }
        },
        {
            "$match": {
                "totalSpent": {"$gte": min_total_spent}  
            }

        },
        {
            "$project": {
                "_id": 0,
                "customerId": "$_id",
                "totalSpent": 1,
                "averageOrderValue": 1,  
                "orderCount": 1,
                "loyaltyTier": 1 ,
                "lastPurchaseDate": 1,
                "isActive": 1
            }
        }
    ]

    result = await Purchase.aggregate(pipeline).to_list(length=None)
    excel_file = generate_excel(result)

    return StreamingResponse(excel_file, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={"Content-Disposition": "attachment; filename=customer_report.xlsx"})
