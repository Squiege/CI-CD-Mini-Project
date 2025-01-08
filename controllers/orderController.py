from models.schemas.orderSchema import OrderSchema
from services import orderService
from flask import request, jsonify

# Create a new order
def create_order():
    order = OrderSchema().load(request.json)
    orderService.create_order(order)
    return jsonify({"message": "Order created successfully"})

# Get all orders
def get_orders():
    orders = orderService.get_orders()
    return jsonify(orders)

# Get a single order
def get_order(order_id):
    order = orderService.get_order(order_id)
    return jsonify(order)

# Update an order
def update_order(order_id):
    order = OrderSchema().load(request.json)
    orderService.update_order(order_id, order)
    return jsonify({"message": "Order updated successfully"})

# Delete an order
def delete_order(order_id):
    orderService.delete_order(order_id)
    return jsonify({"message": "Order deleted successfully"})