from src.product import Product


class Order:
    """Класс Заказ, в котором будет ссылка на то какой товар был куплен,
    количество купленного товара, а также итоговая стоимость.
    В заказе может быть указан только один товар"""

    product: Product
    buy_count: int
    total_amount: float

    def __init__(self, product: Product, buy_count: int) -> None:
        self.product = product
        self.buy_count = buy_count
        self.total_amount = self.product.price * buy_count
        self.product.quantity -= self.buy_count

    def __str__(self) -> str:
        return f"Было приобретено: {self.product.name} - {self.buy_count} шт., на общую сумму {self.total_amount}"
