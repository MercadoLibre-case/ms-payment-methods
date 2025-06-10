import pytest
from app.domain.services.payment_methods_service import PaymentMethodsService
from app.domain.entities.payment_methods import Credit, Debit, CashPayment, PaymentMethods


class FakeRepository:
    @staticmethod
    def get_enabled_payment_methods(product_id, price, currency, category):
        return PaymentMethods(
            credit=Credit(brands=["Visa"]),
            debit=Debit(brands=["Maestro"]),
            cash_payment=CashPayment(payment_type=["PIX"])
        )


def test_service_returns_payment_methods():
    repo = FakeRepository()
    service = PaymentMethodsService(repo)
    result = service.get_enabled_payment_methods("1", 500, "USD", "electronics")
    assert isinstance(result, PaymentMethods)
    assert result.credit.brands == ["Visa"]
