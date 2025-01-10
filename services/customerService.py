from sqlalchemy.orm import Session
from sqlalchemy import select
from models.customer import Customer
from database import db

# Convert Customer object to dictionary
def serialize_customer(customer):
    return {
        "id": customer.id,
        "name": customer.name,
        "email": customer.email
    }

def find_all_customers():
    query = select(Customer)
    customers = db.session.execute(query).scalars().all()
    # Serialize the customers
    return [serialize_customer(customer) for customer in customers]

def find_customer_by_id(customer_id):
    try:
        customer = db.session.query(Customer).filter_by(id=customer_id).first()
        return serialize_customer(customer) if customer else None
    except Exception as e:
        print(f"Error fetching customer by ID: {e}")
        return None

def create_customer(data):
    try:
        new_customer = Customer(name=data['name'], email=data['email'])
        db.session.add(new_customer)
        db.session.commit()
        db.session.refresh(new_customer)
        # Serialize the new customer
        return serialize_customer(new_customer)
    except Exception as e:
        db.session.rollback()
        raise e

def update_customer(customer_id, customer_data):
    try:
        customer = db.session.query(Customer).filter_by(id=customer_id).first()
        if customer:
            customer.name = customer_data.get('name', customer.name)
            customer.email = customer_data.get('email', customer.email)
            db.session.commit()
            # Serialize the updated customer
            return serialize_customer(customer)
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
