class PrintMixin:
    """Класс-миксин для печати в консоль информации о том,
    с какими параметрами был создан объект из класса Product"""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
