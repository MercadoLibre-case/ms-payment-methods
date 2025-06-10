from app.domain.entities.payment_methods import PaymentMethods
from app.domain.interfaces.payment_methods_repository_interface import IPaymentMethodsRepository
from app.shared.exceptions import EmptyEnabledPaymentMethodsException


class PaymentMethodsService:
    def __init__(self, repository: IPaymentMethodsRepository):
        self.repository = repository

    def get_enabled_payment_methods(self, product_id: str, price: float, currency: str, category: str) -> PaymentMethods:
        enabled_payment_methods = self.repository.get_enabled_payment_methods(
            product_id, price, currency, category
        )
        if not enabled_payment_methods:
            raise EmptyEnabledPaymentMethodsException()
        return enabled_payment_methods
