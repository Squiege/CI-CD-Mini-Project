# Importing the necessary libraries
from flask import Flask, jsonify
from database import db
from schema import ma
from limiter import limiter
from sqlalchemy.orm import Session
from flask_swagger_ui import get_swaggerui_blueprint
from config import DevelopmentConfig

from dotenv import load_dotenv
load_dotenv()

# Blueprint Imports
from routes.customerAccountBP import customer_account_blue_print
from routes.orderBP import order_blue_print
from routes.productBP import product_blue_print
from routes.customerBP import customer_blue_print

# Model Imports
from models.customerAccount import CustomerAccount
from models.order import Order
from models.product import Product
from models.customer import Customer
from models.role import Role
from models.customerManagementRole import CustomerManagementRole

# Swagger configuration
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "m13_mp"}
)

def create_app(config=DevelopmentConfig):
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)  
    blue_print_config(app)  
    configure_rate_limit()

    # Get all routes
    @app.route('/routes', methods=['GET'])
    def list_routes():
        routes = []
        for rule in app.url_map.iter_rules():
            routes.append({
                "endpoint": rule.endpoint,
                "methods": list(rule.methods),
                "url": str(rule)
            })
        return jsonify(routes)

    return app

def blue_print_config(app):
    """Register blueprints."""
    app.register_blueprint(customer_account_blue_print, url_prefix='/api/customer-accounts')
    app.register_blueprint(order_blue_print, url_prefix='/api/orders')
    app.register_blueprint(product_blue_print, url_prefix='/api/products')
    app.register_blueprint(customer_blue_print, url_prefix='/api/customers')
    app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

def configure_rate_limit():
    """Configure rate limits for blueprints."""
    limiter.limit("100 per day")(customer_account_blue_print)
    limiter.limit("100 per day")(order_blue_print)
    limiter.limit("100 per day")(product_blue_print)
    limiter.limit("100 per day")(customer_blue_print)

def init_roles_data():
    """Initialize roles data."""
    with Session(db.engine) as session:
        with session.begin():
            roles = [
                Role(id=1, role_name='Admin'),
                Role(id=2, role_name='Manager'),
                Role(id=3, role_name='User')
            ]
            session.add_all(roles)
            print("Roles initialized successfully.")

def init_customers_info_data():
    """Initialize customer and customer account data."""
    with Session(db.engine) as session:
        with session.begin():
            customers = [
                Customer(id=1, name='Customer 1', email='customer1@example.com'),
                Customer(id=2, name='Customer 2', email='customer2@example.com'),
                Customer(id=3, name='Customer 3', email='customer3@example.com')
            ]
            session.add_all(customers)

            customer_accounts = [
                CustomerAccount(id=1, customer_id=1, username='ctm1', password='1234'),
                CustomerAccount(id=2, customer_id=2, username='ctm2', password='1234'),
                CustomerAccount(id=3, customer_id=3, username='ctm3', password='1234')
            ]
            session.add_all(customer_accounts)
            print("Customers and Customer accounts initialized successfully.")

def init_roles_customers_data():
    """Initialize customer management roles data."""
    with Session(db.engine) as session:
        with session.begin():
            roles_customers = [
                CustomerManagementRole(customer_account_id=1, role_id=1),
                CustomerManagementRole(customer_account_id=2, role_id=2),
                CustomerManagementRole(customer_account_id=3, role_id=3)
            ]
            session.add_all(roles_customers)
            print("Customer management roles initialized successfully.")


app = create_app()


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        init_roles_data()
        init_customers_info_data()
        init_roles_customers_data()

    app.run(debug=True)
