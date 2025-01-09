from models.order import Order
from database import db

def find_all_orders():
    try:
        return db.session.query(Order).all()
    except Exception as e:
        print(f"Error fetching orders: {e}")
        return []

def find_order_by_id(order_id):
    try:
        return db.session.query(Order).filter_by(id=order_id).first()
    except Exception as e:
        print(f"Error fetching order by ID: {e}")
        return None

def create_order(order_data):
    try:
        new_order = Order(**order_data)  
        db.session.add(new_order)
        db.session.commit()
        db.session.refresh(new_order)  # Refresh to ensure we return the latest state
        return new_order
    except Exception as e:
        db.session.rollback()
        print(f"Error creating order: {e}")
        return None

def update_order(order_id, order_data):
    try:
        existing_order = db.session.query(Order).filter_by(id=order_id).first()
        if existing_order:
            existing_order.customer_id = order_data.get('customer_id', existing_order.customer_id)
            existing_order.product_id = order_data.get('product_id', existing_order.product_id)
            existing_order.quantity = order_data.get('quantity', existing_order.quantity)
            existing_order.total_price = order_data.get('total', existing_order.total_price)
            db.session.commit()
            db.session.refresh(existing_order)  # Refresh to return the latest state
        return existing_order
    except Exception as e:
        db.session.rollback()
        print(f"Error updating order: {e}")
        return None

def delete_order(order_id):
    try:
        existing_order = db.session.query(Order).filter_by(id=order_id).first()
        if existing_order:
            db.session.delete(existing_order)
            db.session.commit()
            return True
        return False
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting order: {e}")
        return False
