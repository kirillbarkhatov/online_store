import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product1():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def product2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product3():
    return Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14)


@pytest.fixture
def product4():
    return Product(name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7)


@pytest.fixture
def category1(product1, product2, product3):
    return Category(
        name="Смартфоны",
        description="""Смартфоны, как средство не только коммуникации, 
но и получения дополнительных функций для удобства жизни""",
        products=[product1, product2, product3],
    )


@pytest.fixture
def category2(product4):
    return Category(
        name="Телевизоры",
        description="""Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником""",
        products=[product4],
    )


@pytest.fixture
def products_by_category_list_of_dict():
    return [
        {
            "name": "Смартфоны",
            "description": """Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни""",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": """Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником""",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]
