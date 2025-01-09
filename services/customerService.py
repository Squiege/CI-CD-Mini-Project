from sqlalchemy.orm import Session
from models.customer import Customer
from database import db

def find_all_customers():
    try:
        customers = db.session.query(Customer).all()
        return customers
    except Exception as e:
        print(f"Error fetching customers: {e}")
        return []

def find_customer_by_id(customer_id):
    try:
        customer = db.session.query(Customer).filter_by(id=customer_id).first()
        return customer
    except Exception as e:
        print(f"Error fetching customer by ID: {e}")
        return None

def create_customer(customer):
    try:
        db.session.add(customer)
        db.session.commit()
        return customer
    except Exception as e:
        db.session.rollback()
        print(f"Error creating customer: {e}")
        return None

def update_customer(customer_id, customer_data):
    try:
        customer = db.session.query(Customer).filter_by(id=customer_id).first()
        if customer:
            customer.name = customer_data.get('name', customer.name)
            customer.email = customer_data.get('email', customer.email)
            db.session.commit()
            return customer
        return None
    except Exception as e:
        db.session.rollback()
        print(f"Error updating customer: {e}")
        return None

def delete_customer(customer_id):
    try:
        customer = db.session.query(Customer).filter_by(id=customer_id).first()
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return True
        return False
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting customer: {e}")
        return False


