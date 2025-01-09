import unittest
from unittest.mock import patch, MagicMock
from services.orderService import (
    create_order,
    find_order_by_id,
    find_all_orders,
    update_order,
    delete_order,
)
from models.order import Order
from app import app


class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()  # Set up app context
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()  # Pop the app context after each test

    @patch('services.orderService.db.session')
    def test_find_all_orders(self, mock_session):
        # Mock query results
        mock_order1 = Order(id=1, customer_id=1, product_id=1, quantity=2, total_price=50.0)
        mock_order2 = Order(id=2, customer_id=2, product_id=3, quantity=4, total_price=120.0)
        mock_session.query.return_value.all.return_value = [mock_order1, mock_order2]

        orders = find_all_orders()

        self.assertEqual(len(orders), 2)
        self.assertEqual(orders[0].quantity, 2)
        self.assertEqual(orders[1].total_price, 120.0)

    @patch('services.orderService.db.session')
    def test_find_order_by_id(self, mock_session):
        # Mock query result
        mock_order = Order(id=1, customer_id=1, product_id=2, quantity=5, total_price=100.0)
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_order

        order = find_order_by_id(1)

        self.assertIsNotNone(order)
        self.assertEqual(order.customer_id, 1)
        self.assertEqual(order.total_price, 100.0)

    @patch('services.orderService.db.session')
    def test_create_order(self, mock_session):
        # Mock input and expected behavior
        mock_order_data = {'customer_id': 1, 'product_id': 2, 'quantity': 5, 'total_price': 100.0}
        mock_order = Order(id=1, **mock_order_data)

        mock_session.add = MagicMock()
        mock_session.commit = MagicMock()
        mock_session.refresh = MagicMock()
        mock_session.refresh.return_value = mock_order

        created_order = create_order(mock_order_data)

        mock_session.add.assert_called_once_with(mock_order)
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once_with(mock_order)

    @patch('services.orderService.db.session')
    def test_update_order(self, mock_session):
        mock_existing_order = Order(id=1, customer_id=1, product_id=2, quantity=5, total_price=100.0)
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_existing_order

        new_order_data = {'customer_id': 2, 'product_id': 3, 'quantity': 10, 'total_price': 200.0}

        updated_order = update_order(1, new_order_data)

        self.assertEqual(updated_order.customer_id, 2)
        self.assertEqual(updated_order.total_price, 200.0)
        mock_session.commit.assert_called_once()

    @patch('services.orderService.db.session')
    def test_delete_order(self, mock_session):
        mock_existing_order = Order(id=1, customer_id=1, product_id=2, quantity=5, total_price=100.0)
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_existing_order

        delete_order(1)

        mock_session.delete.assert_called_once_with(mock_existing_order)
        mock_session.commit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
