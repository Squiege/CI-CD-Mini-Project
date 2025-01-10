from models.schemas.customerSchema import CustomerSchema
from services import customerService
from flask import request, jsonify

# Helper function to serialize customer objects
def serialize_customer(customer):
    return {
        "id": customer.id,
        "name": customer.name,
        "email": customer.email
    }

# Create a new customer
def create_customer():
    customer_schema = CustomerSchema()
    customer_data = customer_schema.load(request.json)
    new_customer = customerService.create_customer(customer_data)
    if new_customer:
        return jsonify(serialize_customer(new_customer)), 201
    return jsonify({"error": "Failed to create customer"}), 400

# Get all customers
def get_customers():
    customers = customerService.find_all_customers()
    serialized_customers = [serialize_customer(customer) for customer in customers]
    return jsonify(serialized_customers)

# Get a customer by ID
def get_customer_by_id(customer_id):
    customer = customerService.find_customer_by_id(customer_id)
    if customer:
        return jsonify(serialize_customer(customer))
    return jsonify({"error": "Customer not found"}), 404

# Update a customer by ID
def update_customer(customer_id):
    customer_schema = CustomerSchema()
    customer_data = customer_schema.load(request.json)
    updated_customer = customerService.update_customer(customer_id, customer_data)
    if updated_customer:
        return jsonify(serialize_customer(updated_customer))
    return jsonify({"error": "Customer not found"}), 404

# Delete a customer by ID
def delete_customer(customer_id):
    success = customerService.delete_customer(customer_id)
    if success:
        return jsonify({"message": "Customer deleted successfully"}), 200
    return jsonify({"error": "Customer not found"}), 404
