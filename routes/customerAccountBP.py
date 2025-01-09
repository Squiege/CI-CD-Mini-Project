from flask import Blueprint
from controllers.customerAccountController import find_all, find_by_id, delete_by_id, create, update

customer_account_blue_print = Blueprint('customer_account', __name__)

customer_account_blue_print.route('/customer-accounts', methods=['GET'])(find_all)
customer_account_blue_print.route('/<id>', methods=['GET'])(find_by_id)
customer_account_blue_print.route('/delete/<id>', methods=['DELETE'])(delete_by_id)
customer_account_blue_print.route('/create', methods=['POST'])(create)
customer_account_blue_print.route('/update/<id>', methods=['PUT'])(update)