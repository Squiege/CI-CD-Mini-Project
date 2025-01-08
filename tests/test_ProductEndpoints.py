import unittest
from unittest.mock import patch, MagicMock
from services.productService import create_product, find_product_by_id
from models.product import Product
from app import app

class TestProductService(unittest.TestCase):
    @patch('services.productService.Session')
    def test_save_product(self, MockSession):
        with app.app_context():
            mock_product_data = {
                'name': 'Gadget B',
                'price': 49.99
            }

            mock_session_instance = MagicMock()
            MockSession.return_value = mock_session_instance

            mock_product = Product(**mock_product_data)
            mock_session_instance.refresh = MagicMock()

            saved_product = create_product(mock_product_data)

            self.assertEqual(saved_product.name, 'Gadget B')
            self.assertEqual(saved_product.price, 49.99)

            mock_session_instance.add.assert_called_once_with(mock_product)
            mock_session_instance.commit.assert_called_once()
            mock_session_instance.refresh.assert_called_once_with(mock_product)

    @patch('services.productService.db.session')
    def test_get_product_by_id(self, mock_db_session):
        mock_product = MagicMock(id=1, name='Gadget B', price=49.99)
        mock_db_session.query.return_value.filter_by.return_value.first.return_value = mock_product

        product = find_product_by_id(1)

        self.assertEqual(product['id'], 1)
        self.assertEqual(product['name'], 'Gadget B')
        self.assertEqual(product['price'], 49.99)

if __name__ == '__main__':
    unittest.main()
