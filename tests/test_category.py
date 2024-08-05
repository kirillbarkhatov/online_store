import pytest
from unittest.mock import patch


def test_category(capsys, category1, category2, product4):
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
    message = capsys.readouterr()
    assert category2.product_count == 5
    assert message.out.strip().split("\n")[-2] == "Товар успешно добавлен"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"


def test_category_str(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."


def test_category_add_product_error(category2):
    with pytest.raises(TypeError):
        assert category2.add_product("Это не продукт")


def test_middle_price(category1, category_without_products):
    assert category1.middle_price() == 140333.33
    assert category_without_products.middle_price() == 0


def test_custom_exception(capsys, category2, product4):
    product4.quantity = 0
    category2.add_product(product4)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар с нулевым количеством добавить нельзя"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"
