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
        db.session.refresh(new_order)
        return new_order  
    except Exception as e:
        db.session.rollback()
        print(f"Error creating order: {e}")
        return None

def update_order(order_id, order_data):
    try:
        order = db.session.query(Order).filter_by(id=order_id).first()
        if order:
            order.customer_id = order_data.get('customer_id', order.customer_id)
            order.product_id = order_data.get('product_id', order.product_id)
            order.quantity = order_data.get('quantity', order.quantity)
            order.total_price = order_data.get('total_price', order.total_price)
            db.session.commit()
            return order  
        return None
    except Exception as e:
        db.session.rollback()
        print(f"Error updating order: {e}")
        return None

def delete_order(order_id):
    try:
        order = db.session.query(Order).filter_by(id=order_id).first()
        if order:
            db.session.delete(order)
            db.session.commit()
            return True
        return False
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting order: {e}")
        return False
