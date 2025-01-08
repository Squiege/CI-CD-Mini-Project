from sqlalchemy import select
from models.product import Product
from database import db

def find_all_products():
    query = select(Product)
    return db.execute(query).scalars().all()

def find_product_by_id(product_id):
    query = select(Product).filter(Product.id == product_id)
    return db.execute(query).scalar()

def create_product(product):
    db.add(product)
    db.commit()

def update_product(product_id, product):
    query = select(Product).filter(Product.id == product_id)
    existing_product = db.execute(query).scalar()
    existing_product.name = product.name
    existing_product.price = product.price
    db.commit()

def delete_product(product_id):
    query = select(Product).filter(Product.id == product_id)
    existing_product = db.execute(query).scalar()
    db.delete(existing_product)
    db.commit()