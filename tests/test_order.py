from src.order import Order


def test_order(product1):
    assert str(Order(product1, 2)) == "Было приобретено: Samsung Galaxy S23 Ultra - 2 шт., на общую сумму 360000.0"
