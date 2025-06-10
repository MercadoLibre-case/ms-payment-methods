from typing import List


class Credit:
    def __init__(self,
                 brands: List[str]):
        self.brands = brands


class Debit:
    def __init__(self,
                 brands: List[str]):
        self.brands = brands


class CashPayment:
    def __init__(self,
                 payment_type: List[str]):
        self.payment_type = payment_type


class PaymentMethods:
    def __init__(self,
                 credit: Credit,
                 debit: Debit,
                 cash_payment: CashPayment):
        self.credit = credit
        self.debit = debit
        self.cash_payment = cash_payment
