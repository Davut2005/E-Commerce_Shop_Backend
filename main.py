from fastapi import FastAPI
from routers import products, users, categories, reviews, orders, payments
from core.config import settings

app = FastAPI()

app.include_router(products)
app.include_router(users)
app.include_router(categories)
app.include_router(reviews)
app.include_router(orders)
app.include_router(payments)

if __name__ == "__main__" :
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)