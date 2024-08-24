from src.order import Order


def test_order(product1):
    assert str(Order(product1, 2)) == "Было приобретено: Samsung Galaxy S23 Ultra - 2 шт., на общую сумму 360000.0"


def test_custom_exception(capsys, product4):
    product4.quantity = 0
    Order(product4, 2)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар с нулевым количеством добавить в заказ нельзя"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара в заказ завершена"
