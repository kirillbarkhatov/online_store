from src.product import Product
from typing import Any


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(self, name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 country: str,
                 germination_period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Any) -> Any:
        if type(other) is LawnGrass.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError
