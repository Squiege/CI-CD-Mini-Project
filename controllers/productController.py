from models.schemas.productSchema import ProductSchema
from services import productService
from flask import request, jsonify

# Helper function to serialize product objects
def serialize_product(product):
    return {
        "id": product.id,
        "name": product.name,
        "price": product.price
    }

# Create a new product
def create_product():
    product_data = ProductSchema().load(request.json)
    new_product = productService.create_product(product_data)
    if new_product:
        return jsonify(serialize_product(new_product)), 201
    return jsonify({"error": "Failed to create product"}), 400

# Get all products
def get_products():
    products = productService.find_all_products()
    serialized_products = [serialize_product(product) for product in products]
    return jsonify(serialized_products)

# Get a single product
def get_product(product_id):
    product = productService.find_product_by_id(product_id)
    if product:
        return jsonify(serialize_product(product))
    return jsonify({"error": "Product not found"}), 404

# Update a product
def update_product(product_id):
    product_data = ProductSchema().load(request.json)
    updated_product = productService.update_product(product_id, product_data)
    if updated_product:
        return jsonify(serialize_product(updated_product))
    return jsonify({"error": "Product not found"}), 404

# Delete a product
def delete_product(product_id):
    success = productService.delete_product(product_id)
    if success:
        return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"error": "Product not found"}), 404
