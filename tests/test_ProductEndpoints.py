import unittest
from unittest.mock import patch, MagicMock
from services.productService import (
    create_product,
    find_product_by_id,
    find_all_products,
    update_product,
    delete_product,
)
from models.product import Product
from app import app


class TestProductService(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()  # Set up app context
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()  # Pop the app context after each test

    @patch('services.productService.db.session')
    def test_find_all_products(self, mock_session):
        mock_product1 = Product(id=1, name='Product A', price=10.99)
        mock_product2 = Product(id=2, name='Product B', price=20.99)
        mock_session.query.return_value.all.return_value = [mock_product1, mock_product2]

        products = find_all_products()

        self.assertEqual(len(products), 2)
        self.assertEqual(products[0].name, 'Product A')
        self.assertEqual(products[1].price, 20.99)

    @patch('services.productService.db.session')
    def test_find_product_by_id(self, mock_session):
        mock_product = Product(id=1, name='Product A', price=10.99)
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_product

        product = find_product_by_id(1)

        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'Product A')
        self.assertEqual(product.price, 10.99)

    @patch('services.productService.db.session')
    def test_create_product(self, mock_session):
        mock_product_data = {'name': 'Product A', 'price': 10.99}
        mock_product = Product(id=1, **mock_product_data)

        mock_session.add = MagicMock()
        mock_session.commit = MagicMock()
        mock_session.refresh = MagicMock()
        mock_session.refresh.return_value = mock_product

        created_product = create_product(mock_product_data)

        mock_session.add.assert_called_once_with(mock_product)
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once_with(mock_product)

    @patch('services.productService.db.session')
    def test_update_product(self, mock_session):
        mock_existing_product = Product(id=1, name='Product A', price=10.99)
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_existing_product

        new_product_data = {'name': 'Updated Product', 'price': 15.99}

        updated_product = update_product(1, new_product_data)

        self.assertEqual(updated_product.name, 'Updated Product')
        self.assertEqual(updated_product.price, 15.99)
        mock_session.commit.assert_called_once()

    @patch('services.productService.db.session')
    def test_delete_product(self, mock_session):
        mock_existing_product = Product(id=1, name='Product A', price=10.99)
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_existing_product

        delete_product(1)

        mock_session.delete.assert_called_once_with(mock_existing_product)
        mock_session.commit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
