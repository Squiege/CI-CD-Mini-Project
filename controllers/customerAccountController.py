from models.schemas.customerAccountSchema import CustomerAccountSchema
from services import customerAccountService
from flask import request, jsonify

# Find all customer accounts
def find_all():
    customer_accounts = customerAccountService.find_all_accounts()
    return jsonify(CustomerAccountSchema().dump(customer_accounts))

# Find customer account by id
def find_by_id(id):
    customer_account = customerAccountService.find_account_by_id(id)
    return jsonify(CustomerAccountSchema().dump(customer_account))

# Delete customer account by id
def delete_by_id(id):
    customer_account = customerAccountService.delete_account(id)
    return jsonify(CustomerAccountSchema().dump(customer_account))

# Create customer account
def create():
    data = request.get_json()
    customer_account = customerAccountService.create_account(data)
    return jsonify(CustomerAccountSchema().dump(customer_account))

# Update customer account by id
def update(id):
    data = request.get_json()
    customer_account = customerAccountService.update_account(id, data)
    return jsonify(CustomerAccountSchema().dump(customer_account))