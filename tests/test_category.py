def test_category(category1, category2):
    assert category1.name == "Смартфоны"
    assert category2.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"

    assert category1.category_count == 2
    assert category2.product_count == 4
