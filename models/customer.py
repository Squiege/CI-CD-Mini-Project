from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    email = Column(String(320), nullable=False)

    # Relationships
    orders = relationship('Order', back_populates='customer')
    customer_account = relationship('CustomerAccount', back_populates='customer')
