from sqlalchemy import select
from models.order import Order
from database import db

def find_all_orders():
    query = select(Order)
    return db.execute(query).scalars().all()

def find_order_by_id(order_id):
    query = select(Order).filter(Order.id == order_id)
    return db.execute(query).scalar()

def create_order(order):
    db.add(order)
    db.commit()

def update_order(order_id, order):
    query = select(Order).filter(Order.id == order_id)
    existing_order = db.execute(query).scalar()
    existing_order.customer_id = order.customer_id
    existing_order.product_id = order.product_id
    existing_order.quantity = order.quantity
    existing_order.total = order.total
    db.commit()

def delete_order(order_id):
    query = select(Order).filter(Order.id == order_id)
    existing_order = db.execute(query).scalar()
    db.delete(existing_order)
    db.commit()
