from abc import ABC, abstractmethod
from app.domain.entities.payment_methods import PaymentMethods

class IPaymentMethodsRepository(ABC):

    @abstractmethod
    def get_enabled_payment_methods(self, product_id: str, price: float, currency: str, category: str) -> PaymentMethods:
        pass