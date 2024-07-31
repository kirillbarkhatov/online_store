class PrintMixin:
    """Класс-миксин для печати в консоль информации о том,
    с какими параметрами был создан объект из класса Product"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
