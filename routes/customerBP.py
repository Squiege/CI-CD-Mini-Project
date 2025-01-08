from flask import Blueprint
from controllers.customerController import create_customer, get_customers, get_customer_by_id, update_customer, delete_customer

customer_blue_print = Blueprint('customer', __name__)

customer_blue_print.route('/customer/create', methods=['POST'])(create_customer)
customer_blue_print.route('/customers', methods=['GET'])(get_customers)
customer_blue_print.route('/customer/<customer_id>', methods=['GET'])(get_customer_by_id)
customer_blue_print.route('/customer/update/<customer_id>', methods=['PUT'])(update_customer)
customer_blue_print.route('/customer/delete/<customer_id>', methods=['DELETE'])(delete_customer)