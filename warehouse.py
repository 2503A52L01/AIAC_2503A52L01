class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_value(self):
        return self.price * self.quantity


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def most_valuable_product(self):
        if not self.products:
            return None
        return max(self.products, key=lambda product: product.calculate_value())

    def display_most_valuable_product(self):
        product = self.most_valuable_product()
        if product:
            return f'Most Valuable Product: {product.name}, Value: {product.calculate_value()}'
        return 'No products in warehouse.'