from flask import Blueprint
from controllers.orderController import create_order, get_orders, get_order, update_order, delete_order

order_blue_print = Blueprint('order', __name__)

order_blue_print.route('/create', methods=['POST'])(create_order)
order_blue_print.route('/', methods=['GET'])(get_orders)
order_blue_print.route('/<order_id>', methods=['GET'])(get_order)
order_blue_print.route('/update/<order_id>', methods=['PUT'])(update_order)
order_blue_print.route('/delete/<order_id>', methods=['DELETE'])(delete_order)

