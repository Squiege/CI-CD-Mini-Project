from models.schemas.productSchema import ProductSchema
from services import productService
from flask import request, jsonify

# Create a new product
def create_product():
    product = ProductSchema().load(request.json)
    productService.create_product(product)
    return jsonify({"message": "Product created successfully"})

# Get all products
def get_products():
    products = productService.get_products()
    return jsonify(products)

# Get a single product
def get_product(product_id):
    product = productService.get_product(product_id)
    return jsonify(product)

# Update a product
def update_product(product_id):
    product = ProductSchema().load(request.json)
    productService.update_product(product_id, product)
    return jsonify({"message": "Product updated successfully"})

# Delete a product
def delete_product(product_id):
    productService.delete_product(product_id)
    return jsonify({"message": "Product deleted successfully"})