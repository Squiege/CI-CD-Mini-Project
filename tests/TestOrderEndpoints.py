import unittest
from unittest.mock import patch, MagicMock
from services.orderService import create_order, find_order_by_id
from models.order import Order
from app import app

class TestOrderService(unittest.TestCase):
    @patch('services.orderService.Session')
    def test_save_order(self, MockSession):
        with app.app_context():
            mock_order_data = {
                'customer_id': 1,
                'product_id': 2,
                'quantity': 5
            }

            mock_session_instance = MagicMock()
            MockSession.return_value = mock_session_instance

            mock_order = Order(**mock_order_data)
            mock_session_instance.refresh = MagicMock()

            saved_order = create_order(mock_order_data)

            self.assertEqual(saved_order.customer_id, 1)
            self.assertEqual(saved_order.product_id, 2)
            self.assertEqual(saved_order.quantity, 5)

            mock_session_instance.add.assert_called_once_with(mock_order)
            mock_session_instance.commit.assert_called_once()
            mock_session_instance.refresh.assert_called_once_with(mock_order)

    @patch('services.orderService.db.session')
    def test_get_order(self, mock_db_session):
        mock_order = MagicMock(id=1, customer_id=1, product_id=2, quantity=5, total_price=100.0)
        mock_db_session.query.return_value.filter.return_value.first.return_value = mock_order

        order = find_order_by_id(1)

        self.assertEqual(order['id'], 1)
        self.assertEqual(order['total_price'], 100.0)
        self.assertEqual(order['customer_id'], 1)

if __name__ == '__main__':
    unittest.main()
