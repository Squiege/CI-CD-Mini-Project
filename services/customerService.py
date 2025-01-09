from sqlalchemy.orm import Session
from models.customer import Customer
from database import db

def find_all_customers():
    with db.session as session:  
        return session.query(Customer).all()

def find_customer_by_id(customer_id):
    with db.session as session:
        return session.query(Customer).filter_by(id=customer_id).first()

def create_customer(customer_data):
    with db.session as session:
        new_customer = Customer(**customer_data)  
        session.add(new_customer)
        session.commit()
        session.refresh(new_customer)  
        return new_customer

def update_customer(customer_id, customer_data):
    with db.session as session:
        existing_customer = session.query(Customer).filter_by(id=customer_id).first()
        if existing_customer:
            existing_customer.name = customer_data['name']
            existing_customer.email = customer_data['email']
            session.commit()
            session.refresh(existing_customer)  
        return existing_customer

def delete_customer(customer_id):
    with db.session as session:
        existing_customer = session.query(Customer).filter_by(id=customer_id).first()
        if existing_customer:
            session.delete(existing_customer)
            session.commit()


