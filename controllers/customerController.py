from models.schemas.customerSchema import CustomerSchema
from services import customerService
from flask import request, jsonify

# Create a new customer
def create_customer():
    customer_schema = CustomerSchema()
    customer = customer_schema.load(request.json)
    result = customerService.create_customer(customer)
    return jsonify(result)

# Get all customers
def get_customers():
    result = customerService.get_customers()
    return jsonify(result)

# Get a customer by ID
def get_customer_by_id(customer_id):
    result = customerService.get_customer_by_id(customer_id)
    return jsonify(result)

# Update a customer by ID
def update_customer(customer_id):
    customer_schema = CustomerSchema()
    customer = customer_schema.load(request.json)
    result = customerService.update_customer(customer_id, customer)
    return jsonify(result)

# Delete a customer by ID
def delete_customer(customer_id):
    result = customerService.delete_customer(customer_id)
    return jsonify(result)