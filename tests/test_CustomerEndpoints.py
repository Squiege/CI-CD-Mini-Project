import unittest
from unittest.mock import patch, MagicMock
from services.customerService import create_customer
from models.customer import Customer
from app import app

class TestCustomerService(unittest.TestCase):
    @patch('services.customerService.Session')
    def test_save_customer(self, MockSession):
        with app.app_context():
            mock_customer_data = {
                'name': 'Alice Johnson',
                'email': 'alice.johnson@example.com',
            }

            mock_session_instance = MagicMock()
            MockSession.return_value = mock_session_instance

            mock_customer = Customer(**mock_customer_data)
            mock_session_instance.refresh = MagicMock()

            saved_customer = create_customer(mock_customer_data)

            self.assertEqual(saved_customer.name, 'Alice Johnson')
            self.assertEqual(saved_customer.email, 'alice.johnson@example.com')

            mock_session_instance.add.assert_called_once_with(mock_customer)
            mock_session_instance.commit.assert_called_once()
            mock_session_instance.refresh.assert_called_once_with(mock_customer)

if __name__ == '__main__':
    unittest.main()