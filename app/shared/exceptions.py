class ApplicationException(Exception):
    """Exceção base para erros da aplicação."""
    pass


class ProductNotFoundException(ApplicationException):
    """Exceção lançada quando um produto não é encontrado."""

    def __init__(self, product_id: str):
        super().__init__(f"Produto com ID '{product_id}' não encontrado.")
        self.product_id = product_id


class EmptyProductListException(ApplicationException):
    """Exceção lançada quando a lista de produtos vier Nula"""

    def __init__(self):
        super().__init__("Lista de produtos está vazia.")


class EmptyEnabledPaymentMethodsException(ApplicationException):
    """Exceção lançada quando não houverem meios de pagamento disponíveis"""

    def __init__(self):
        super().__init__("Não há meios de pagamento disponíveis para este produto")

class EmptyProductRequestException(ApplicationException):
    """Exceção lançada quando não houverem dados para consulta no request"""

    def __init__(self):
        super().__init__("Request Vazio")
