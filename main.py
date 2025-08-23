# filepath: python-ai-product-warehouse/python-ai-product-warehouse/src/main.py
from product import Product
from warehouse import Warehouse

warehouse = Warehouse()

# Take product entries from user
num_products = int(input("How many products do you want to add? "))
for i in range(num_products):
    name = input(f"Enter name for product {i+1}: ")
    price = float(input(f"Enter price for product {i+1}: "))
    quantity = int(input(f"Enter quantity for product {i+1}: "))
    product = Product(name, price, quantity)
    warehouse.add_product(product)

# Display most valuable product
most_valuable = warehouse.most_valuable_product()
print(f"Most valuable product: {most_valuable.name} (${most_valuable.calculate_value()})")