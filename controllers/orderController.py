from models.schemas.orderSchema import OrderSchema
from services import orderService
from flask import request, jsonify

# Helper function to serialize order objects
def serialize_order(order):
    return {
        "id": order.id,
        "customer_id": order.customer_id,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "total_price": order.total_price
    }

# Create a new order
def create_order():
    order_data = OrderSchema().load(request.json)
    new_order = orderService.create_order(order_data)
    if new_order:
        return jsonify(serialize_order(new_order)), 201
    return jsonify({"error": "Failed to create order"}), 400

# Get all orders
def get_orders():
    orders = orderService.find_all_orders()
    serialized_orders = [serialize_order(order) for order in orders]
    return jsonify(serialized_orders)

# Get a single order
def get_order(order_id):
    order = orderService.find_order_by_id(order_id)
    if order:
        return jsonify(serialize_order(order))
    return jsonify({"error": "Order not found"}), 404

# Update an order
def update_order(order_id):
    order_data = OrderSchema().load(request.json)
    updated_order = orderService.update_order(order_id, order_data)
    if updated_order:
        return jsonify(serialize_order(updated_order))
    return jsonify({"error": "Order not found"}), 404

# Delete an order
def delete_order(order_id):
    success = orderService.delete_order(order_id)
    if success:
        return jsonify({"message": "Order deleted successfully"}), 200
    return jsonify({"error": "Order not found"}), 404
