from typing import Any, Iterator

from src.category import Category


class ProductIterator:
    category_with_products: Category
    index: int

    def __init__(self, category_with_products: Category):
        self.category_with_products = category_with_products

    def __iter__(self) -> Iterator:
        self.index = 0
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category_with_products.products_list):
            product = self.category_with_products.products_list[self.index]
            self.index += 1
            return product

        else:
            raise StopIteration
