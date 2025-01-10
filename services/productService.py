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
        db.session.refresh(new_product)
        return new_product  
    except Exception as e:
        db.session.rollback()
        print(f"Error creating product: {e}")
        return None

def update_product(product_id, product_data):
    try:
        product = db.session.query(Product).filter_by(id=product_id).first()
        if product:
            product.name = product_data.get('name', product.name)
            product.price = product_data.get('price', product.price)
            db.session.commit()
            return product  
        return None
    except Exception as e:
        db.session.rollback()
        print(f"Error updating product: {e}")
        return None

def delete_product(product_id):
    try:
        product = db.session.query(Product).filter_by(id=product_id).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting product: {e}")
        return False
