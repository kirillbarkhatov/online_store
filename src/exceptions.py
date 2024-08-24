class ZeroQuantityProduct(Exception):
    """Исключение, которое отвечает за обработку событий,
    когда в Категорию или в Заказ добавляется товар с нулевым количеством"""

    def __init__(self, message: str) -> None:
        super().__init__(message)
