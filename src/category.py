class Category:
    name: str
    description: str
    products: list
    count_of_categories = 0
    count_of_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.count_of_categories += 1
        Category.count_of_products += len(products)
