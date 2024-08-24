from typing import Any

from src.exceptions import ZeroQuantityProduct
from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    category_count: int = 0
    product_count: int = 0
    total_products_quantity: int

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        self.total_products_quantity = 0
        for product in self.__products:
            self.total_products_quantity += product.quantity
        return f"{self.name}, количество продуктов: {self.total_products_quantity} шт."

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{product}\n"
        return product_str

    @property
    def products_list(self) -> Any:
        return self.__products

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct("Товар с нулевым количеством добавить нельзя")
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар успешно добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    def middle_price(self) -> Any:
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
