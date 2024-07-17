class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")

        elif self.__price > price:
            answer = input("Подтвердите снижение цены [y/n]: ").lower()
            if answer == "y":
                self.__price = price
            else:
                print("Цена не была изменена")

        else:
            self.__price = price

    @classmethod
    def new_product(cls, new_product: dict, products_list: list = None):
        if products_list is None:
            return cls(**new_product)
        for product in products_list:
            if new_product["name"] == product.name:
                new_product["quantity"] += product.quantity
                if product.price > new_product["price"]:
                    new_product["price"] = product.price

        return cls(**new_product)
