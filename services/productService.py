from sqlalchemy.orm import Session
from models.product import Product
from database import db

def find_all_products():
    with db.session as session:  
        query = session.query(Product)
        return query.all()

def find_product_by_id(product_id):
    with db.session as session:
        return session.query(Product).filter_by(id=product_id).first()

def create_product(product_data):
    with db.session as session:
        new_product = Product(**product_data)  
        session.add(new_product)
        session.commit()
        session.refresh(new_product)  
        return new_product

def update_product(product_id, product_data):
    with db.session as session:
        existing_product = session.query(Product).filter_by(id=product_id).first()
        if existing_product:
            existing_product.name = product_data['name']
            existing_product.price = product_data['price']
            session.commit()
            session.refresh(existing_product)  
        return existing_product

def delete_product(product_id):
    with db.session as session:
        existing_product = session.query(Product).filter_by(id=product_id).first()
        if existing_product:
            session.delete(existing_product)
            session.commit()
