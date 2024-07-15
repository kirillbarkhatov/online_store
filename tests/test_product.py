def test_product(product1, product2, product3, product4):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product2.description == "512GB, Gray space"
    assert product3.price == 31000.0
    assert product4.quantity == 7


def test_category(category1, category2):
    assert category1.name == "Смартфоны"
    assert category2.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"

    assert category1.category_count == 2
    assert category2.product_count == 4

