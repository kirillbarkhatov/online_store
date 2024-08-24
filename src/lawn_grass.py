from typing import Any

from src.product import Product


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Any) -> Any:
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
