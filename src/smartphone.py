from src.product import Product
from typing import Any


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 efficiency: float,
                 model: str,
                 memory: int,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Any) -> Any:
        if type(other) is Smartphone.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError