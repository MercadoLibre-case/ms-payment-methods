from fastapi import FastAPI
from app.controllers.payment_methods_controller import router as product_router

app = FastAPI(title="Payment Methods Microservice")

app.include_router(product_router, prefix="/payment")
