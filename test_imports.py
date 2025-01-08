import sys
import os

print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

try:
    from services.customerService import create_customer
    print("Successfully imported 'create_customer' from 'services.customerService'")
except ModuleNotFoundError as e:
    print(f"Error importing 'create_customer': {e}")

try:
    from models.customer import Customer
    print("Successfully imported 'Customer' from 'models.customer'")
except ModuleNotFoundError as e:
    print(f"Error importing 'Customer': {e}")

try:
    from app import app
    print("Successfully imported 'app' from 'app.py'")
except ModuleNotFoundError as e:
    print(f"Error importing 'app': {e}")
