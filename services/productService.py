from models.product import Product
from database import db

def find_all_products():
    try:
        return db.session.query(Product).all()
    except Exception as e:
        print(f"Error fetching products: {e}")
        return []

def find_product_by_id(product_id):
    try:
        return db.session.query(Product).filter_by(id=product_id).first()
    except Exception as e:
        print(f"Error fetching product by ID: {e}")
        return None

def create_product(product_data):
    try:
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        db.session.refresh(new_product)  # Refresh to return the latest state
        return new_product
    except Exception as e:
        db.session.rollback()
        print(f"Error creating product: {e}")
        return None

def update_product(product_id, product_data):
    try:
        existing_product = db.session.query(Product).filter_by(id=product_id).first()
        if existing_product:
            existing_product.name = product_data.get('name', existing_product.name)
            existing_product.price = product_data.get('price', existing_product.price)
            db.session.commit()
            db.session.refresh(existing_product)  # Refresh to return the latest state
        return existing_product
    except Exception as e:
        db.session.rollback()
        print(f"Error updating product: {e}")
        return None

def delete_product(product_id):
    try:
        existing_product = db.session.query(Product).filter_by(id=product_id).first()
        if existing_product:
            db.session.delete(existing_product)
            db.session.commit()
            return True
        return False
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting product: {e}")
        return False
