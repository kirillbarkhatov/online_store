from unittest.mock import patch

from src.product import Product

import pytest


def test_product(capsys, product1, product2, product3, product4):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product2.description == "512GB, Gray space"
    assert product3.price == 31000.0
    assert product4.quantity == 7

    product3.price = 40000
    assert product3.price == 40000
    product3.price = 0
    captured = capsys.readouterr()
    assert captured.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    assert product3.price == 40000

    with patch("builtins.input") as mock_input:
        mock_input.return_value = "y"
        product3.price = 100
        assert product3.price == 100

    with patch("builtins.input") as mock_input:
        mock_input.return_value = "n"
        product3.price = 50
        captured = capsys.readouterr()
        assert captured.out == "Цена не была изменена\n"
        assert product3.price == 100

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
    )

    assert new_product.name == "Samsung Galaxy S23 Ultra"

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 160000.0,
            "quantity": 5,
        },
        [product1, product2, product3, product4],
    )

    assert new_product.quantity == 10
    assert new_product.price == 180000.0


def test_product_add(product1, product2):
    assert product1 + product2 == 2580000.0


def test_product_error():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product(
            name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=0
        )
