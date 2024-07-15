import json

from src.category import Category
from src.product import Product
from typing import Any


def read_json(filepath: str) -> Any:
    """Функция обеспечивает данных из файла JSON"""

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def create_products_by_categories_from_dict(products_by_categories: dict) -> list:
    """Функция обеспечивает подгрузку данных по категориями и товарам из подготовленного словаря"""

    categories_list = []
    for category in products_by_categories:
        products_list = []
        for product in category["products"]:
            products_list.append(Product(**product))
        category["products"] = products_list
        categories_list.append(Category(**category))

    return categories_list
