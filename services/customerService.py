from sqlalchemy import select
from models.customer import Customer
from database import db

def find_all_customers():
    query = select(Customer)
    return db.execute(query).scalars().all()

def find_customer_by_id(customer_id):
    query = select(Customer).filter(Customer.id == customer_id)
    return db.execute(query).scalar()

def create_customer(customer):
    db.add(customer)
    db.commit()

def update_customer(customer_id, customer):
    query = select(Customer).filter(Customer.id == customer_id)
    existing_customer = db.execute(query).scalar()
    existing_customer.name = customer.name
    existing_customer.email = customer.email
    db.commit()

def delete_customer(customer_id):
    query = select(Customer).filter(Customer.id == customer_id)
    existing_customer = db.execute(query).scalar()
    db.delete(existing_customer)
    db.commit()

