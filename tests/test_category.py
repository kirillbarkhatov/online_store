import pytest


def test_category(category1, category2, product4):
    assert category1.name == "Смартфоны"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

    assert category1.category_count == 2
    assert category2.product_count == 4
    assert (
        category1.products
        == """Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"""
    )
    category2.add_product(product4)
    assert category2.product_count == 5


def test_category_str(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."


def test_category_add_product_error(category2):
    with pytest.raises(TypeError):
        assert category2.add_product("Это не продукт")
