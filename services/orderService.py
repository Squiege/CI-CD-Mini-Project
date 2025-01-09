from sqlalchemy.orm import Session
from models.order import Order
from database import db

def find_all_orders():
    with db.session as session:  
        return session.query(Order).all()

def find_order_by_id(order_id):
    with db.session as session:
        return session.query(Order).filter_by(id=order_id).first()

def create_order(order_data):
    with db.session as session:
        new_order = Order(**order_data)  
        session.add(new_order)
        session.commit()
        session.refresh(new_order) 
        return new_order

def update_order(order_id, order_data):
    with db.session as session:
        existing_order = session.query(Order).filter_by(id=order_id).first()
        if existing_order:
            existing_order.customer_id = order_data['customer_id']
            existing_order.product_id = order_data['product_id']
            existing_order.quantity = order_data['quantity']
            existing_order.total = order_data['total']
            session.commit()
            session.refresh(existing_order)  
        return existing_order

def delete_order(order_id):
    with db.session as session:
        existing_order = session.query(Order).filter_by(id=order_id).first()
        if existing_order:
            session.delete(existing_order)
            session.commit()

