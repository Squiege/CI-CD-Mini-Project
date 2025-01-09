from flask import Blueprint
from controllers.productController import get_products, get_product, delete_product, update_product, create_product

product_blue_print = Blueprint('product', __name__)

product_blue_print.route('/', methods=['GET'])(get_products)
product_blue_print.route('/<int:id>', methods=['GET'])(get_product)
product_blue_print.route('/delete/<int:id>', methods=['DELETE'])(delete_product)
product_blue_print.route('/update/<int:id>', methods=['PUT'])(update_product)
product_blue_print.route('/create', methods=['POST'])(create_product)