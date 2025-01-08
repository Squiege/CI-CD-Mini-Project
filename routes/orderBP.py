from flask import Blueprint
from controllers.orderController import create_order, get_orders, get_order, update_order, delete_order

order_blue_print = Blueprint('order', __name__)

order_blue_print.route('/order/create', methods=['POST'])(create_order)
order_blue_print.route('/orders', methods=['GET'])(get_orders)
order_blue_print.route('/order/<order_id>', methods=['GET'])(get_order)
order_blue_print.route('/order/update/<order_id>', methods=['PUT'])(update_order)
order_blue_print.route('/order/delete/<order_id>', methods=['DELETE'])(delete_order)

