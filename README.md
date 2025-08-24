# python-product-warehouse

## Overview
This project implements a simple inventory management system using Python. It consists of two main classes: `Product` and `Warehouse`. The `Product` class represents an item with a name, price, and quantity, while the `Warehouse` class manages a collection of products and provides functionality to add products and determine the most valuable product in stock.

## Classes

### Product
- **Attributes:**
  - `name`: The name of the product.
  - `price`: The price of the product.
  - `quantity`: The quantity of the product in stock.
  
- **Methods:**
  - `__init__(self, name, price, quantity)`: Initializes a new product with the specified name, price, and quantity.
  - `calculate_value(self)`: Returns the total value of the product (price multiplied by quantity).

### Warehouse
- **Attributes:**
  - `products`: A list that stores `Product` objects.
  
- **Methods:**
  - `add_product(self, product)`: Adds a `Product` object to the warehouse.
  - `most_valuable_product(self)`: Returns the product with the highest total value.

## Experience with AI Code Completion
During the development of this project, AI-powered code suggestions were utilized to enhance productivity and streamline the coding process. The suggestions helped in generating class structures, method definitions, allowing for a more efficient workflow and reducing the likelihood of errors.

## Installation
To install the required dependencies, please refer to the `requirements.txt` file.

## Usage
To use the classes defined in this project, import them from the `src` package and create instances of `Product` and `Warehouse` as needed (main.py) is an example for this.