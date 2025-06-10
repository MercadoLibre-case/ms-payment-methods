from fastapi import APIRouter, HTTPException
from app.dtos.payment_methods_schema import PaymentMethodsSchema, PaymentRequestSchema
from app.dtos.mapper import payment_methods_to_schema
from app.domain.services.payment_methods_service import PaymentMethodsService
from app.infrastructure.data.payment_methods_repository_json import PaymentMethodsRepositoryJson
from app.shared.exceptions import EmptyEnabledPaymentMethodsException, EmptyProductRequestException

router = APIRouter()

repository = PaymentMethodsRepositoryJson("app/infrastructure/data/payment-methods.json")
service = PaymentMethodsService(repository)


@router.post("/payment-methods", response_model=PaymentMethodsSchema)
def get_enabled_payment_methods(product_input: PaymentRequestSchema):
    try:
        payment_methods = service.get_enabled_payment_methods(
            product_id=product_input.product_id,
            price=product_input.price,
            currency=product_input.currency,
            category=product_input.category
        )
        return payment_methods_to_schema(payment_methods)
    except EmptyEnabledPaymentMethodsException as em:
        raise HTTPException(status_code=204, detail=str(em))
    except EmptyProductRequestException as emp:
        raise HTTPException(status_code=422, detail=str(emp))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
