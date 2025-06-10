import json
from pathlib import Path
from app.domain.entities.payment_methods import Credit, Debit, CashPayment, PaymentMethods
from app.domain.interfaces.payment_methods_repository_interface import IPaymentMethodsRepository


class PaymentMethodsRepositoryJson(IPaymentMethodsRepository):
    def __init__(self, data_file: str):
        self.data_file = Path(data_file)

    def _load_data(self):
        with open(self.data_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_enabled_payment_methods(self, product_id: str, price: float, currency: str,
                                    category: str) -> PaymentMethods:
        data = self._load_data()
        payment_config = data["payment-methods"]

        credit_brands = payment_config["credit"]["brands"]
        debit_brands = payment_config["debit"]["brands"]
        cash_methods = payment_config["cash_payment"]["payment_type"]

        if price < 100:
            credit_brands = credit_brands[:3]  # Limita bandeiras como exemplo
            cash_methods = ["PIX"]
        elif price > 500:
            cash_methods = ["PIX", "Boleto"]

        if category == "clothing":
            cash_methods = [m for m in cash_methods if m != "Boleto"]

        return PaymentMethods(
            credit=Credit(brands=credit_brands),
            debit=Debit(brands=debit_brands),
            cash_payment=CashPayment(payment_type=cash_methods)
        )
