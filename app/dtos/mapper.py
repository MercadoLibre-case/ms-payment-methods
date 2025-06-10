from app.domain.entities.payment_methods import PaymentMethods
from app.dtos.payment_methods_schema import PaymentMethodsSchema, CreditSchema, DebitSchema, CashPaymentSchema


def payment_methods_to_schema(payment_methods: PaymentMethods) -> PaymentMethodsSchema:
    return PaymentMethodsSchema(
        credit=CreditSchema(
            brands=payment_methods.credit.brands
        ),
        debit=DebitSchema(
            brands=payment_methods.debit.brands
        ),
        cash_payment=CashPaymentSchema(
            payment_type=payment_methods.cash_payment.payment_type
        )
    )
