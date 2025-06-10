from typing import List

from pydantic import BaseModel


class CreditSchema(BaseModel):
    brands: List[str]


class DebitSchema(BaseModel):
    brands: List[str]


class CashPaymentSchema(BaseModel):
    payment_type: List[str]


class PaymentMethodsSchema(BaseModel):
    credit: CreditSchema
    debit: DebitSchema
    cash_payment: CashPaymentSchema


class PaymentRequestSchema(BaseModel):
    product_id: str
    price: float
    currency: str
    category: str
