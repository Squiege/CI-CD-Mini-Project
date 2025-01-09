import unittest
from unittest.mock import patch, MagicMock
from services.customerService import (
    create_customer,
    find_customer_by_id,
    find_all_customers,
    update_customer,
    delete_customer,
)
from models.customer import Customer
from app import app


class TestCustomerService(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch('services.customerService.db.session')
    def test_find_all_customers(self, mock_session):
        mock_session.__enter__.return_value = mock_session
        mock_customer1 = Customer(id=1, name='Alice Johnson', email='alice@example.com')
        mock_customer2 = Customer(id=2, name='Bob Smith', email='bob@example.com')
        mock_session.query.return_value.all.return_value = [mock_customer1, mock_customer2]

        customers = find_all_customers()

        self.assertEqual(len(customers), 2)
        self.assertEqual(customers[0].name, 'Alice Johnson')
        self.assertEqual(customers[1].email, 'bob@example.com')

    @patch('services.customerService.db.session')
    def test_find_customer_by_id(self, mock_session):
        mock_session.__enter__.return_value = mock_session
        mock_customer = Customer(id=1, name='Alice Johnson', email='alice@example.com')
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_customer

        customer = find_customer_by_id(1)

        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, 'Alice Johnson')
        self.assertEqual(customer.email, 'alice@example.com')

    @patch('services.customerService.db.session')
    def test_create_customer(self, mock_session):
        mock_session.__enter__.return_value = mock_session
        mock_session.add = MagicMock()
        mock_session.commit = MagicMock()
        mock_session.refresh = MagicMock()

        mock_customer_data = {'name': 'Alice Johnson', 'email': 'alice.johnson@example.com'}
        mock_customer = Customer(id=1, **mock_customer_data)
        mock_session.refresh.return_value = mock_customer

        created_customer = create_customer(mock_customer_data)

        mock_session.add.assert_called_once_with(mock_customer)
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once_with(mock_customer)
        self.assertEqual(created_customer.name, 'Alice Johnson')
        self.assertEqual(created_customer.email, 'alice.johnson@example.com')

    @patch('services.customerService.db.session')
    def test_update_customer(self, mock_session):
        mock_session.__enter__.return_value = mock_session
        mock_existing_customer = Customer(id=1, name='Alice Johnson', email='alice@example.com')
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_existing_customer

        new_customer_data = {'name': 'Updated Name', 'email': 'updated@example.com'}

        updated_customer = update_customer(1, new_customer_data)

        self.assertEqual(updated_customer.name, 'Updated Name')
        self.assertEqual(updated_customer.email, 'updated@example.com')
        mock_session.commit.assert_called_once()

    @patch('services.customerService.db.session')
    def test_delete_customer(self, mock_session):
        mock_session.__enter__.return_value = mock_session
        mock_existing_customer = Customer(id=1, name='Alice Johnson', email='alice@example.com')
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_existing_customer

        delete_customer(1)

        mock_session.delete.assert_called_once_with(mock_existing_customer)
        mock_session.commit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
